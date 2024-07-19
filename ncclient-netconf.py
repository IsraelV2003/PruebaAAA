import xml.dom.minidom
from ncclient import manager

# Conexión al servidor NETCONF
m = manager.connect(
    host="192.168.56.104",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)

# Obtener la configuración actual
netconf_reply = m.get_config(source="running")
print("Configuración Actual:")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# Obtener la configuración con un filtro específico
netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""
netconf_reply = m.get_config(source="running", filter=netconf_filter)
print("Configuración con Filtro:")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# Configuración del hostname
netconf_hostname = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
     <hostname>IsraelValverde</hostname>
  </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_hostname)
print("Configuración del Hostname:")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# Agregar una nueva interfaz Loopback
netconf_loopback = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>1</name>
    <description>My first NETCONF loopback</description>
    <ip>
     <address>
      <primary>
       <address>10.7.7.7</address>
       <mask>255.255.255.0</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_loopback)
print("Configuración del Loopback 1:")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# Agregar una segunda interfaz Loopback
netconf_newloop = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>2</name>
    <description>My second NETCONF loopback</description>
    <ip>
     <address>
      <primary>
       <address>10.1.1.1</address>
       <mask>255.255.255.0</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_newloop)
print("Configuración del Loopback 2:")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

