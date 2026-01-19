import xml.etree.ElementTree as ET

xml_path = "distribution.xml"

tree = ET.parse(xml_path)
root = tree.getroot()

# title変更
title = root.find("title")
if title is None:
    title = ET.SubElement(root, "title")
title.text = "My Awesome App"

# options 追加・変更
options = root.find("options")
if options is None:
    options = ET.SubElement(root, "options")

options.set("customize", "never")
options.set("require-scripts", "false")

# background 追加
background = root.find("background")
if background is None:
    background = ET.SubElement(root, "background")

background.set("file", "background.png")
background.set("alignment", "bottomleft")
background.set("scaling", "tofit")

# domains 設定
domains = root.find("domains")
if domains is None:
    domains = ET.SubElement(root, "domains")

domains.set("enable_anywhere", "false")
domains.set("enable_currentUserHome", "false")
domains.set("enable_localSystem", "true")

# installation-check
check = root.find("installation-check")
if check is None:
    check = ET.SubElement(root, "installation-check")
check.set("script", "checkOS()")

# script
script = root.find("script")
if script is None:
    script = ET.SubElement(root, "script")

script.text = """
<![CDATA[
function checkOS() {
    var os = system.version.ProductVersion;
    if (compareVersions(os, "11.0") < 0) {
        my.result.title = "macOS のバージョンが古すぎます";
        my.result.message = "このアプリは macOS 11.0 以上が必要です。";
        my.result.type = "Fatal";
        return false;
    }
    return true;
}
]]>
"""
# 保存
tree.write(xml_path, encoding="utf-8", xml_declaration=True)
