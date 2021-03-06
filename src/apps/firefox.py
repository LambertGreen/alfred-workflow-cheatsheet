# coding: utf8
shortcuts = {
    "Firefox":{
        #https://support.mozilla.org/en-US/kb/keyboard-shortcuts-perform-firefox-tasks-quickly
        #https://developer.mozilla.org/en-US/docs/Tools/Page_Inspector/Keyboard_shortcuts
        "Navigation - Back    ":"⌘← or ⌘[ or ⌫",
        "Navigation - Forward ":"⌘→ or ⌘] or ⇧⌫",
        "Navigation - Home   ":"⌥ home",
        "Navigation - Open File   ":"⌘O",
        "Navigation - Reload  ":"F5 or ⌘R",
        "Navigation - Reload (override cache) ":"⌘⇧R",
        "Navigation - Stop    ":"Esc  or ⌘.",
        "Current Page - Go Down a Screen    ":"fn↓",
        "Current Page - Go Up a Screen  ":"fn↑ or ⇧Space",
        "Current Page - Go to Bottom of Page    ":"End or ⌘↓",
        "Current Page - Go to Top of Page   ":"Home or ⌘↑",
        "Current Page - Move to Next Frame  ":"F6",
        "Current Page - Move to Previous Frame  ":"⇧F6",
        "Current Page - Print   ":"⌘P",
        "Current Page - Save Page As    ":"⌘S",
        "Current Page - Zoom In ":"⌘+",
        "Current Page - Zoom Out    ":"⌘-",
        "Current Page - Zoom Reset  ":"⌘0",
        "Editing - Copy    ":"⌘C",
        "Editing - Cut ":"⌘X",
        "Editing - Delete  ":"⌫",
        "Editing - Paste  ":"⌘V",
        "Editing - Paste (as plain text)   ":"⌘⇧V",
        "Editing - Redo    ":"⌘⇧Z",
        "Editing - Select All  ":"⌘A",
        "Editing - Undo    ":"⌘Z",
        "Search - Find    ":"⌘F ",
        "Search - Find Again  ":"F3 or ⌘G ",
        "Search - Find Previous   ":"⇧F3 or ⌘⇧G ",
        "Search - Quick Find within link-text only    ":"'   ",
        "Search - Quick Find  ":"/   ",
        "Search - Close the Find or Quick Find bar    ":"Esc - when the Find or Quick Find bar is focused",
        "Search - Focus Search bar    ":"⌘K or ⌘⌥F    ",
        "Search - Quickly switch between search engines   ":"⌘↑ or ⌘↓ - when Search Bar is focused",
        "Search - View menu to switch, add or manage search engines":"⌥↑ or ⌥↓  - when Search Bar is focused",
        "Windows/tabs - Close Tab   ":"⌘W - except for App Tabs",
        "Windows/tabs - Close Window    ":"⌘⇧W ",
        "Windows/tabs - Move Tab in focus Left  ":"^⇧Page Up  ",
        "Windows/tabs - Move Tab in focus ":"Right ^⇧Page Down    ",
        "Windows/tabs - Move Tab in focus to start  ":"⌘home  ",
        "Windows/tabs - Move Tab in focus to end    ":"⌘end   ",
        "Windows/tabs - Mute/Unmute Audio   ":"^M    ",
        "Windows/tabs - New Tab ":"⌘T ",
        "Windows/tabs - New Window  ":"⌘N ",
        "Windows/tabs - New Private Window  ":"⌘⇧P ",
        "Windows/tabs - Next Tab    ":"⌥tab or ⌥ page down or ⌘⌥→    ",
        "Windows/tabs - Open Address in New Tab ":"⏎- from Location Bar or Search Bar",
        "Windows/tabs - Previous Tab    ":"⌥⇧tab or ⌥ page up or ⌘⌥←    ",
        "Windows/tabs - Undo Close Tab  ":"⌘⇧T ",
        "Windows/tabs - Undo Close Window   ":"⌘⇧N ",
        "Windows/tabs - Select Tab 1 to 8   ":"⌘1to8  ",
        "Windows/tabs - Select Last Tab ":"⌘9",
        "History - History sidebar ":"⌘⇧H",
        "History - Clear Recent History    ":"⌘⇧⌫",
        "Bookmarks - Bookmark All Tabs   ":"⌘⇧D",
        "Bookmarks - Bookmark This Page  ":"⌘D",
        "Bookmarks - Bookmarks sidebar   ":"⌘B",
        "Bookmarks - Library window  ":"⌘⇧B",
        "Tools - Downloads   ":"⌘J",
        "Tools - Add-ons ":"⌘⇧A",
        "Tools - Toggle Developer Tools  ":"F12 or ⌘⌥I",
        "Tools - Web Console ":"⌘⌥K",
        "Tools - Inspector   ":"⌘⌥C",
        "Tools - Debugger    ":"⌘⌥S",
        "Tools - Style Editor    ":"⇧F7",
        "Tools - Profiler    ":"⇧F5",
        "Tools - Network ":"⌘⌥Q",
        "Tools - Developer Toolbar   ":"⇧F2",
        "Tools - Responsive Design View  ":"⌘⌥M",
        "Tools - Scratchpad  ":"⇧F4",
        "Tools - Page Source ":"⌘U",
        "Tools - Browser Console ":"⌘⇧J",
        "Tools - Page Info   ":"⌘I",
        "PDF Viewer - Next page   ":"N or J or →",
        "PDF Viewer - Previous page   ":"P or K or ←",
        "PDF Viewer - Zoom in ":"⌘+",
        "PDF Viewer - Zoom out    ":"⌘-",
        "PDF Viewer - Automatic Zoom  ":"⌘0",
        "PDF Viewer - Rotate the document clockwise   ":"R",
        "PDF Viewer - Rotate counterclockwise ":"⇧R",
        "PDF Viewer - Switch to Presentation Mode ":"⌘⌥P",
        "PDF Viewer - Toggle Hand Tool    ":"H",
        "PDF Viewer - Focus the Page Number input box ":"⌘⌥G",
        "Complete .com Address   ":"⌘⏎",
        "Complete .net Address   ":"⇧⏎",
        "Complete .org Address   ":"⌘⇧⏎",
        "Delete Selected Autocomplete Entry  ":"⇧⌫",
        "Toggle Full Screen  ":"⌘⇧F",
        "Toggle Reader Mode  ":"⌘⌥R",
        "Caret Browsing  ":"F7",
        "Select Location Bar ":"F6 or ⌘L",
        "Media - Toggle Play / Pause ":"Space",
        "Media - Decrease volume ":"↓",
        "Media - Increase volume ":"↑",
        "Media - Mute audio  ":"⌘↓",
        "Media - Unmute audio    ":"⌘↑",
        "Media - Seek back 15 seconds    ":"←",
        "Media - Seek back 10 %  ":"⌘←",
        "Media - Seek forward 15 seconds ":"→",
        "Media - Seek forward 10 %   ":"⌘→",
        "Media - Seek to the beginning   ":"Home",
        "Media - Seek to the end ":"End",
        "Inspect Element":"⌘⌥C",
        "Node picker - Select the element under the mouse and cancel picker mode   ":"Click",
        "Node picker - Select the element under the mouse and stay in picker mode   ":"⇧Click ",
        "HTML pane - Delete the selected node    ":"⌫",
        "HTML pane - Undo delete of a node   ":"⌘Z",
        "HTML pane - Redo delete of a node   ":"⌘⇧Z / ⌘Y",
        "HTML pane - Move to next node (expanded nodes only) ":"↓",
        "HTML pane - Move to previous node   ":"↑",
        "HTML pane - Expand currently selected node  ":"→",
        "HTML pane - Collapse currently selected node    ":"→",
        "HTML pane - Step forward through the attributes of a node   ":"Tab",
        "HTML pane - Step backward through the attributes of a node  ":"⇧Tab",
        "HTML pane - Start editing the selected attribute    ":"⏎",
        "HTML pane - Hide/show the selected node ":"H",
        "HTML pane - Focus on the search box in the HTML pane    ":"⌘F",
        "HTML pane - Edit as HTML    ":"F2",
        "HTML pane - Stop editing HTML   ":"F2 / ^⏎",
        "HTML pane - Copy the selected node's outer HTML  ":"⌘C",
        "HTML pane - Scroll the selected node into view   ":"S",
        "HTML pane - Find the next match in the markup, when searching is active ":"⏎",
        "HTML pane - Find the previous match in the markup, when searching is active  ":"⇧⏎",
        "Breadcrumbs bar - Move to the previous element in the breadcrumbs bar     ":"←",
        "Breadcrumbs bar - Move to the next element in the breadcrumbs bar     ":"→",
        "Breadcrumbs bar - Focus the HTML pane ":"⇧Tab",
        "Focus the CSS pane  ":"Tab",
        "CSS pane - Focus on the search box in the CSS pane ":"⌘F",
        "CSS pane - Clear search box content (only when the search box is focused, and content has been entered)    ":"Esc",
        "CSS pane - Step forward through properties and values  ":"Tab",
        "CSS pane - Step backward through properties and values ":"⇧Tab",
        "CSS pane - Start editing property or value (Rules view only, when a property or value is selected, but not already being edited)   ":"⏎ or Space",
        "CSS pane - Cycle up and down through auto-complete suggestions (Rules view only, when a property or value is being edited) ":"↑, ↓",
        "CSS pane - Choose current auto-complete suggestion (Rules view only, when a property or value is being edited) ":"⏎ or Tab",
        "CSS pane - Increment selected value by 1   ":"↑",
        "CSS pane - Decrement selected value by 1   ":"↓",
        "CSS pane - Increment selected value by 100 ":"⇧Page Up",
        "CSS pane - Decrement selected value by 100 ":"⇧Page Down",
        "CSS pane - Increment selected value by 10  ":"⇧↑",
        "CSS pane - Decrement selected value by 10  ":"⇧↓",
        "CSS pane - Increment selected value by 0.1 ":"⌥↑",
        "CSS pane - Decrement selected value by 0.1 ":"⌥↓",
        "CSS pane - Show/hide more information about current property (Computed view only, when a property is selected)  ":"⏎ or Space",
        "CSS pane - Open MDN reference page about current property (Computed view only, when a property is selected) ":"F1",
        "CSS pane - Open current CSS file in Style Editor (Computed view only, when more information is shown for a property and a CSS file reference is focused)    ":"⏎`",
        "Increase font size  ":"⌘+",
        "Decrease font size  ":"⌘-",
        "Reset font size ":"⌘0"
    }
}