from fanstatic import Library, Resource

library = Library('js.ace', 'resources')

ace = Resource(library, 'ace.js')

# All resources from ace-build subdir "src-min-noconflict" are copied into
# this packge, but only frequently used resources are defined as Resource
# objects.

mode_html        = Resource(library, 'mode-html.js')
mode_javascript  = Resource(library, 'mode-javascript.js')
mode_json        = Resource(library, 'mode-json.js')
mode_xml         = Resource(library, 'mode-xml.js')

worker_javascript = Resource(library, 'worker-javascript.js')
