#-----------------------------------------------------------------------------
# WTF is this shiz?:   * Update popup [mediaInfos ]fields in a list of webmaps
# popupInfo: https://developers.arcgis.com/web-map-specification/objects/popupInfo/
# field_infos = item_data['operationalLayers'][0]['layers'][0]['popupInfo']['mediaInfos']
#-----------------------------------------------------------------------------

import arcgis
import json

##PARAMETERS

#ENV:
AGOL = "arcgis.com"

#source:
src = AGOL
src_admin = ""
src_admin_pwd = ""
src_owner = ""

#webmap paramenters:

#item id of webmaps
item_id = [
    #eg: itemid of webmaps
    "76345t4c7335467abee40653940963ed",
    "cbd4k6149cf04275afd5d69a512dca3b",
    "6ef345688d1b74ae5b11f889bac781148"
    ]
mapservice_id = "OtherWSLNonAssets_6481"
layer_id = 0

#modify text:
update = [{
            "title":"",
            "type":"image",
            "caption":"",
            "value":{
                "sourceURL":"configs/PopupPanel/link.png",
                "linkURL": "https://wsldcttgweb.water.internal/GISApps/dbquery/query.aspx?servno={SERVNO}&type=page"
            }
         }]

#access portal params
gis = arcgis.gis.GIS("https://" + src, src_admin, src_admin_pwd, verify_cert=False)

#function
def modifyPopupInfos( mapservice_id, layer_id, update):
    for layers in layers_infos:
    #finds the layer
        if layers['id'] == mapservice_id:
            print ("target ID: "+str(layers['layers'][1]['popupInfo']['title']))
            for lyr in layers['layers']:
                if lyr['id'] == layer_id:
                    print("  ID: " + str(lyr['id']),"Title: " +  str(lyr['popupInfo']['title']))
                    print("    before: " +  str(lyr['popupInfo']['mediaInfos']))
                    lyr['popupInfo']['mediaInfos'] = update                           
                    print("    after: " +  str(lyr['popupInfo']['mediaInfos']))
        else:
            print(".")
    item_properties = {"text": json.dumps(item_data)}
    item.update(item_properties=item_properties)
    return

#start script:
for i in item_id:
    print (i)
    item = gis.content.get(i)
    item_data = item.get_data()
    layers_infos = item_data['operationalLayers']
    modifyPopupInfos(mapservice_id, layer_id, update)


