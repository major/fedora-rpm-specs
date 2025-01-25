#
# Rebuild option:
#
#   --with testsuite         - run the test suite (requires X)
#

# NOTE: On every new version, we need to manually regenerate the list of XS Provides
# cd Wx-*
# for i in `grep -r "PACKAGE=" * | cut -d " " -f 2 | sed 's|PACKAGE=|perl(|g' | grep "Wx::" | sort -n |uniq`; do printf "Provides: $i)\\n"; done &> provides.txt
# grep -orP '%name{Wx::[^}]*}\s+class' |grep -v "3pm" | cut -d : -f 2- | sed 's|%name{|Provides: perl(|g' | sed 's|} class|)|g' |uniq &>> provides.txt
# cat provides.txt | uniq | sort -n

Name:           perl-Wx
Version:        0.9932
Release:        38%{?dist}
Summary:        Interface to the wxWidgets cross-platform GUI toolkit
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Wx
Source0:        https://cpan.metacpan.org/authors/id/M/MD/MDOOTSON/Wx-%{version}.tar.gz
# Work around BOM_UTF8 clash between wxGTK and Perl. Should be fixed in newer
# wxGTK, CPAN RT#121464, <http://trac.wxwidgets.org/ticket/13599>.
Patch0:         Wx-0.9932-Undefine-BOM_UTF8.patch
Patch1:         gtk3.patch
Patch2:         wxWidgets_3.2_MakeMaker.patch
Patch3:         wxWidgets_3.2_port.patch
BuildRequires:  make
BuildRequires:  wxGTK-devel
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Alien::wxWidgets) >= 0.25
BuildRequires:  perl(blib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.21
BuildRequires:  perl(ExtUtils::ParseXS) >= 2.2203
BuildRequires:  perl(ExtUtils::XSpp::Cmd)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Info)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More), perl(Test::Harness)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(YAML) >= 0.35
BuildRequires:  dos2unix

# this package requires the same version of perl(Alien::wxWidgets::Config::gtk_XXX) it was built with
# see https://bugzilla.redhat.com/2232294 for details.
# oh, we crossing the streams here, hold on.
%global alien_versioned_require %(rpm -q perl-Alien-wxWidgets --provides |grep gtk)

%if "%{alien_versioned_require}" != ""
Requires: %{alien_versioned_require}
%endif

# Manual provides from XS
Provides: perl(Wx::AboutDialogInfo)
Provides: perl(Wx::AcceleratorEntry)
Provides: perl(Wx::AcceleratorTable)
Provides: perl(Wx::ActivateEvent)
Provides: perl(Wx::ANIHandler)
Provides: perl(Wx::Animation)
Provides: perl(Wx::AnimationCtrl)
Provides: perl(Wx::_App)
Provides: perl(Wx::App)
Provides: perl(Wx::ArchiveFSHandler)
Provides: perl(Wx::ArrayStringProperty)
Provides: perl(Wx::ArtProvider)
Provides: perl(Wx::AUI)
Provides: perl(Wx::AuiManager)
Provides: perl(Wx::AuiManagerEvent)
Provides: perl(Wx::AuiNotebook)
Provides: perl(Wx::AuiNotebookEvent)
Provides: perl(Wx::AuiPaneInfo)
Provides: perl(Wx::AutoBufferedPaintDC)
Provides: perl(Wx::BannerWindow)
Provides: perl(Wx::BestHelpController)
Provides: perl(Wx::Bitmap)
Provides: perl(Wx::BitmapBundle)
Provides: perl(Wx::BitmapButton)
Provides: perl(Wx::BitmapComboBox)
Provides: perl(Wx::BitmapDataObject)
Provides: perl(Wx::BitmapToggleButton)
Provides: perl(Wx::BMPHandler)
Provides: perl(Wx::BookCtrl)
Provides: perl(Wx::BookCtrlEvent)
Provides: perl(Wx::BoolProperty)
Provides: perl(Wx::BoxSizer)
Provides: perl(Wx::Brush)
Provides: perl(Wx::BufferedDC)
Provides: perl(Wx::BufferedPaintDC)
Provides: perl(Wx::BusyCursor)
Provides: perl(Wx::BusyInfo)
Provides: perl(Wx::Button)
Provides: perl(Wx::CalendarCtrl)
Provides: perl(Wx::CalendarDateAttr)
Provides: perl(Wx::CalendarEvent)
Provides: perl(Wx::Caret)
Provides: perl(Wx::CaretSuspend)
Provides: perl(Wx::CheckBox)
Provides: perl(Wx::CheckListBox)
Provides: perl(Wx::ChildFocusEvent)
Provides: perl(Wx::CHMHelpController)
Provides: perl(Wx::Choice)
Provides: perl(Wx::Choicebook)
Provides: perl(Wx::ClassInfo)
Provides: perl(Wx::Client)
Provides: perl(Wx::ClientDC)
Provides: perl(Wx::Clipboard)
Provides: perl(Wx::ClipboardTextEvent)
Provides: perl(Wx::CloseEvent)
Provides: perl(Wx::CollapsiblePane)
Provides: perl(Wx::CollapsiblePaneEvent)
Provides: perl(Wx::Colour)
Provides: perl(Wx::ColourData)
Provides: perl(Wx::ColourDatabase)
Provides: perl(Wx::ColourDialog)
Provides: perl(Wx::ColourPickerCtrl)
Provides: perl(Wx::ColourPickerEvent)
Provides: perl(Wx::ColourProperty)
Provides: perl(Wx::ColourPropertyValue)
Provides: perl(Wx::ComboBox)
Provides: perl(Wx::ComboCtrl)
Provides: perl(Wx::ComboPopup)
Provides: perl(Wx::Command)
Provides: perl(Wx::CommandEvent)
Provides: perl(Wx::CommandLinkButton)
Provides: perl(Wx::CommandProcessor)
Provides: perl(Wx::ConfigBase)
Provides: perl(Wx::Connection)
Provides: perl(Wx::ContextHelp)
Provides: perl(Wx::ContextHelpButton)
Provides: perl(Wx::ContextMenuEvent)
Provides: perl(Wx::Control)
Provides: perl(Wx::ControlWithItems)
Provides: perl(Wx::CURHandler)
Provides: perl(Wx::Cursor)
Provides: perl(Wx::CursorProperty)
Provides: perl(Wx::DataFormat)
Provides: perl(Wx::DatagramSocket)
Provides: perl(Wx::DataObject)
Provides: perl(Wx::DataObjectComposite)
Provides: perl(Wx::DataObjectSimple)
Provides: perl(Wx::DataView)
Provides: perl(Wx::DataViewBitmapRenderer)
Provides: perl(Wx::DataViewColumn)
Provides: perl(Wx::DataViewCtrl)
Provides: perl(Wx::DataViewDateRenderer)
Provides: perl(Wx::DataViewEvent)
Provides: perl(Wx::DataViewIconText)
Provides: perl(Wx::DataViewIconTextRenderer)
Provides: perl(Wx::DataViewIndexListModel)
Provides: perl(Wx::DataViewItem)
Provides: perl(Wx::DataViewItemAttr)
Provides: perl(Wx::DataViewListCtrl)
Provides: perl(Wx::DataViewListStore)
Provides: perl(Wx::DataViewModel)
Provides: perl(Wx::DataViewModelNotifier)
Provides: perl(Wx::DataViewProgressRenderer)
Provides: perl(Wx::DataViewRenderer)
Provides: perl(Wx::DataViewSpinRenderer)
Provides: perl(Wx::DataViewTextRenderer)
Provides: perl(Wx::DataViewTextRendererAttr)
Provides: perl(Wx::DataViewToggleRenderer)
Provides: perl(Wx::DataViewTreeCtrl)
Provides: perl(Wx::DataViewTreeStore)
Provides: perl(Wx::DataViewVirtualListModel)
Provides: perl(Wx::DateEvent)
Provides: perl(Wx::DatePickerCtrl)
Provides: perl(Wx::DateProperty)
Provides: perl(Wx::DateSpan)
Provides: perl(Wx::DateTime)
Provides: perl(Wx::DC)
Provides: perl(Wx::DCClipper)
Provides: perl(Wx::DCOverlay)
Provides: perl(Wx::Dialog)
Provides: perl(Wx::DirDialog)
Provides: perl(Wx::DirPickerCtrl)
Provides: perl(Wx::DirProperty)
Provides: perl(Wx::Display)
Provides: perl(Wx::DocChildFrame)
Provides: perl(Wx::DocManager)
Provides: perl(Wx::DocMDIChildFrame)
Provides: perl(Wx::DocMDIParentFrame)
Provides: perl(Wx::DocParentFrame)
Provides: perl(Wx::DocTemplate)
Provides: perl(Wx::Document)
Provides: perl(Wx::DropFilesEvent)
Provides: perl(Wx::DropSource)
Provides: perl(Wx::DropTarget)
Provides: perl(Wx::EditableListBox)
Provides: perl(Wx::EditEnumProperty)
Provides: perl(Wx::EnumProperty)
Provides: perl(Wx::EraseEvent)
Provides: perl(Wx::Event)
Provides: perl(Wx::EventBlocker)
Provides: perl(Wx::EventFilter)
Provides: perl(Wx::EvtHandler)
Provides: perl(Wx::FileConfig)
Provides: perl(Wx::FileCtrl)
Provides: perl(Wx::FileCtrlEvent)
Provides: perl(Wx::FileDataObject)
Provides: perl(Wx::FileDialog)
Provides: perl(Wx::FileDirPickerEvent)
Provides: perl(Wx::FileDropTarget)
Provides: perl(Wx::FileHistory)
Provides: perl(Wx::FilePickerCtrl)
Provides: perl(Wx::FileProperty)
Provides: perl(Wx::FileSystem)
Provides: perl(Wx::FileSystemHandler)
Provides: perl(Wx::FileType)
Provides: perl(Wx::FileTypeInfo)
Provides: perl(Wx::FindDialogEvent)
Provides: perl(Wx::FindReplaceData)
Provides: perl(Wx::FindReplaceDialog)
Provides: perl(Wx::FlagsProperty)
Provides: perl(Wx::FlexGridSizer)
Provides: perl(Wx::FloatProperty)
Provides: perl(Wx::FocusEvent)
Provides: perl(Wx::Font)
Provides: perl(Wx::FontData)
Provides: perl(Wx::FontDialog)
Provides: perl(Wx::FontEnumerator)
Provides: perl(Wx::FontMapper)
Provides: perl(Wx::FontPickerCtrl)
Provides: perl(Wx::FontPickerEvent)
Provides: perl(Wx::FontProperty)
Provides: perl(Wx::Frame)
Provides: perl(Wx::FSFile)
Provides: perl(Wx::Gauge)
Provides: perl(Wx::GBPosition)
Provides: perl(Wx::GBSizerItem)
Provides: perl(Wx::GBSpan)
Provides: perl(Wx::GCDC)
Provides: perl(Wx::GenericDirCtrl)
Provides: perl(Wx::GIFHandler)
Provides: perl(Wx::GraphicsBrush)
Provides: perl(Wx::GraphicsContext)
Provides: perl(Wx::GraphicsFont)
Provides: perl(Wx::GraphicsGradientStop)
Provides: perl(Wx::GraphicsGradientStops)
Provides: perl(Wx::GraphicsMatrix)
Provides: perl(Wx::GraphicsObject)
Provides: perl(Wx::GraphicsPath)
Provides: perl(Wx::GraphicsPen)
Provides: perl(Wx::GraphicsRenderer)
Provides: perl(Wx::Grid)
Provides: perl(Wx::GridBagSizer)
Provides: perl(Wx::GridCellAttr)
Provides: perl(Wx::GridCellAutoWrapStringEditor)
Provides: perl(Wx::GridCellAutoWrapStringRenderer)
Provides: perl(Wx::GridCellBoolEditor)
Provides: perl(Wx::GridCellBoolRenderer)
Provides: perl(Wx::GridCellChoiceEditor)
Provides: perl(Wx::GridCellCoords)
Provides: perl(Wx::GridCellDateTimeRenderer)
Provides: perl(Wx::GridCellEditor)
Provides: perl(Wx::GridCellEnumEditor)
Provides: perl(Wx::GridCellEnumRenderer)
Provides: perl(Wx::GridCellFloatEditor)
Provides: perl(Wx::GridCellFloatRenderer)
Provides: perl(Wx::GridCellNumberEditor)
Provides: perl(Wx::GridCellNumberRenderer)
Provides: perl(Wx::GridCellRenderer)
Provides: perl(Wx::GridCellStringRenderer)
Provides: perl(Wx::GridCellTextEditor)
Provides: perl(Wx::GridEditorCreatedEvent)
Provides: perl(Wx::GridEvent)
Provides: perl(Wx::GridRangeSelectEvent)
Provides: perl(Wx::GridSizeEvent)
Provides: perl(Wx::GridSizer)
Provides: perl(Wx::GridTableBase)
Provides: perl(Wx::GridTableMessage)
Provides: perl(Wx::GridUpdateLocker)
Provides: perl(Wx::HeaderColumn)
Provides: perl(Wx::HeaderColumnSimple)
Provides: perl(Wx::HeaderCtrl)
Provides: perl(Wx::HeaderCtrlEvent)
Provides: perl(Wx::HeaderCtrlSimple)
Provides: perl(Wx::HelpControllerBase)
Provides: perl(Wx::HelpControllerHelpProvider)
Provides: perl(Wx::HelpEvent)
Provides: perl(Wx::HelpProvider)
Provides: perl(Wx::HScrolledWindow)
Provides: perl(Wx::HtmlCell)
Provides: perl(Wx::HtmlCellEvent)
Provides: perl(Wx::HtmlColourCell)
Provides: perl(Wx::HtmlContainerCell)
Provides: perl(Wx::HtmlDCRenderer)
Provides: perl(Wx::HtmlEasyPrinting)
Provides: perl(Wx::HtmlFontCell)
Provides: perl(Wx::HtmlHelpController)
Provides: perl(Wx::HtmlLinkEvent)
Provides: perl(Wx::HtmlLinkInfo)
Provides: perl(Wx::HtmlListBox)
Provides: perl(Wx::HtmlParser)
Provides: perl(Wx::HtmlPrintout)
Provides: perl(Wx::HtmlTag)
Provides: perl(Wx::HtmlTagHandler)
Provides: perl(Wx::HtmlWidgetCell)
Provides: perl(Wx::HtmlWindow)
Provides: perl(Wx::HtmlWinParser)
Provides: perl(Wx::HtmlWinTagHandler)
Provides: perl(Wx::HtmlWordCell)
Provides: perl(Wx::HVScrolledWindow)
Provides: perl(Wx::HyperlinkCtrl)
Provides: perl(Wx::HyperlinkEvent)
Provides: perl(Wx::ICOHandler)
Provides: perl(Wx::Icon)
Provides: perl(Wx::IconBundle)
Provides: perl(Wx::IconizeEvent)
Provides: perl(Wx::IconLocation)
Provides: perl(Wx::IdleEvent)
Provides: perl(Wx::IFFHandler)
Provides: perl(Wx::Image)
Provides: perl(Wx::ImageFileProperty)
Provides: perl(Wx::ImageHandler)
Provides: perl(Wx::ImageList)
Provides: perl(Wx::IndividualLayoutConstraint)
Provides: perl(Wx::InfoBar)
Provides: perl(Wx::InitDialogEvent)
Provides: perl(Wx::InputStream)
Provides: perl(Wx::InternetFSHandler)
Provides: perl(Wx::IntProperty)
Provides: perl(Wx::IPaddress)
Provides: perl(Wx::IPV4address)
Provides: perl(Wx::IPV6address)
Provides: perl(Wx::ItemContainer)
Provides: perl(Wx::ItemContainerImmutable)
Provides: perl(Wx::JoystickEvent)
Provides: perl(Wx::JPEGHandler)
Provides: perl(Wx::KeyEvent)
Provides: perl(Wx::LanguageInfo)
Provides: perl(Wx::LayoutConstraints)
Provides: perl(Wx::Listbook)
Provides: perl(Wx::ListBox)
Provides: perl(Wx::ListCtrl)
Provides: perl(Wx::ListEvent)
Provides: perl(Wx::ListItem)
Provides: perl(Wx::ListItemAttr)
Provides: perl(Wx::ListView)
Provides: perl(Wx::Locale)
Provides: perl(Wx::Log)
Provides: perl(Wx::LogChain)
Provides: perl(Wx::LogFormatter)
Provides: perl(Wx::LogGui)
Provides: perl(Wx::LogNull)
Provides: perl(Wx::LogPassThrough)
Provides: perl(Wx::LogRecordInfo)
Provides: perl(Wx::LogStderr)
Provides: perl(Wx::LogTextCtrl)
Provides: perl(Wx::LogWindow)
Provides: perl(Wx::LongStringProperty)
Provides: perl(Wx::Mask)
Provides: perl(Wx::MaximizeEvent)
Provides: perl(Wx::MDIChildFrame)
Provides: perl(Wx::MDIParentFrame)
Provides: perl(Wx::MediaCtrl)
Provides: perl(Wx::MediaEvent)
Provides: perl(Wx::MemoryDC)
Provides: perl(Wx::MemoryFSHandler)
Provides: perl(Wx::Menu)
Provides: perl(Wx::MenuBar)
Provides: perl(Wx::MenuEvent)
Provides: perl(Wx::MenuItem)
Provides: perl(Wx::MessageDialog)
Provides: perl(Wx::MimeTypesManager)
Provides: perl(Wx::MiniFrame)
Provides: perl(Wx::MirrorDC)
Provides: perl(Wx::MouseCaptureChangedEvent)
Provides: perl(Wx::MouseCaptureLostEvent)
Provides: perl(Wx::MouseEvent)
Provides: perl(Wx::MoveEvent)
Provides: perl(Wx::MultiChoiceDialog)
Provides: perl(Wx::MultiChoiceProperty)
Provides: perl(Wx::NativeFontInfo)
Provides: perl(Wx::NavigationKeyEvent)
Provides: perl(Wx::NewClass)
Provides: perl(Wx::Notebook)
Provides: perl(Wx::NotebookEvent)
Provides: perl(Wx::NotebookSizer)
Provides: perl(Wx::NotificationMessage)
Provides: perl(Wx::NotifyEvent)
Provides: perl(Wx::NumberEntryDialog)
Provides: perl(Wx::OutputStream)
Provides: perl(Wx::Overlay)
Provides: perl(Wx::OwnerDrawnComboBox)
Provides: perl(Wx::PageSetupDialog)
Provides: perl(Wx::PageSetupDialogData)
Provides: perl(Wx::PaintDC)
# Provides: perl(Wx::PaintEvent)
Provides: perl(Wx::Palette)
Provides: perl(Wx::Panel)
Provides: perl(Wx::PasswordEntryDialog)
Provides: perl(Wx::PCXHandler)
Provides: perl(Wx::Pen)
Provides: perl(Wx::PerlTestAbstractNonObject)
Provides: perl(Wx::PerlTestAbstractObject)
Provides: perl(Wx::PerlTestNonObject)
Provides: perl(Wx::PerlTestObject)
Provides: perl(Wx::PGArrayEditorDialog)
Provides: perl(Wx::PGArrayStringEditorDialog)
Provides: perl(Wx::PGCell)
Provides: perl(Wx::PGCellRenderer)
Provides: perl(Wx::PGCheckBoxEditor)
Provides: perl(Wx::PGChoiceAndButtonEditor)
Provides: perl(Wx::PGChoiceEditor)
Provides: perl(Wx::PGChoiceEntry)
Provides: perl(Wx::PGChoices)
Provides: perl(Wx::PGChoicesData)
Provides: perl(Wx::PGComboBoxEditor)
Provides: perl(Wx::PGDatePickerCtrlEditor)
Provides: perl(Wx::PGEditor)
Provides: perl(Wx::PGEditorDialogAdapter)
Provides: perl(Wx::PGFileDialogAdapter)
Provides: perl(Wx::PGLongStringDialogAdapter)
Provides: perl(Wx::PGMultiButton)
Provides: perl(Wx::PGPGridInterfaceBase)
Provides: perl(Wx::PGProperty)
Provides: perl(Wx::PGSpinCtrlEditor)
Provides: perl(Wx::PGTextCtrlAndButtonEditor)
Provides: perl(Wx::PGTextCtrlEditor)
Provides: perl(Wx::PGValidationInfo)
Provides: perl(Wx::PGVIterator)
Provides: perl(Wx::PGWindowList)
Provides: perl(Wx::PickerBase)
Provides: perl(Wx::PlArtProvider)
Provides: perl(Wx::PlCommand)
Provides: perl(Wx::PlCommandEvent)
Provides: perl(Wx::PlDataObjectSimple)
Provides: perl(Wx::PlDataViewIndexListModel)
Provides: perl(Wx::PlEvent)
Provides: perl(Wx::PlEventFilter)
Provides: perl(Wx::PlFileSystemHandler)
Provides: perl(Wx::PlGridCellEditor)
Provides: perl(Wx::PlGridCellRenderer)
Provides: perl(Wx::PlHScrolledWindow)
Provides: perl(Wx::PlHtmlListBox)
Provides: perl(Wx::PlHtmlTagHandler)
Provides: perl(Wx::PlHtmlWinTagHandler)
Provides: perl(Wx::PlHVScrolledWindow)
Provides: perl(Wx::PlLog)
Provides: perl(Wx::PlLogFormatter)
Provides: perl(Wx::PlLogPassThrough)
Provides: perl(Wx::PlOwnerDrawnComboBox)
Provides: perl(Wx::PlPopupTransientWindow)
Provides: perl(Wx::PlPreviewControlBar)
Provides: perl(Wx::PlPreviewFrame)
Provides: perl(Wx::PlRichTextFileHandler)
Provides: perl(Wx::PlSizer)
Provides: perl(Wx::PlThreadEvent)
Provides: perl(Wx::PlValidator)
Provides: perl(Wx::PlVListBox)
Provides: perl(Wx::PlVScrolledWindow)
Provides: perl(Wx::PlWindow)
Provides: perl(Wx::PlXmlResourceHandler)
Provides: perl(Wx::PNGHandler)
Provides: perl(Wx::PNMHandler)
Provides: perl(Wx::Point)
Provides: perl(Wx::PopupTransientWindow)
Provides: perl(Wx::PopupWindow)
Provides: perl(Wx::Position)
Provides: perl(Wx::PowerEvent)
Provides: perl(Wx::PreviewCanvas)
Provides: perl(Wx::PreviewControlBar)
Provides: perl(Wx::PreviewFrame)
Provides: perl(Wx::PrintData)
Provides: perl(Wx::PrintDialog)
Provides: perl(Wx::PrintDialogData)
Provides: perl(Wx::Printer)
Provides: perl(Wx::PrinterDC)
Provides: perl(Wx::PrintFactory)
Provides: perl(Wx::Printout)
Provides: perl(Wx::PrintPaperDatabase)
Provides: perl(Wx::PrintPaperType)
Provides: perl(Wx::PrintPreview)
Provides: perl(Wx::Process)
Provides: perl(Wx::ProcessEvent)
Provides: perl(Wx::ProgressDialog)
Provides: perl(Wx::PropertyAccessor)
Provides: perl(Wx::PropertyCategory)
Provides: perl(Wx::PropertyGrid)
Provides: perl(Wx::PropertyGridEvent)
Provides: perl(Wx::PropertyGridHitTestResult)
Provides: perl(Wx::PropertyGridIterator)
Provides: perl(Wx::PropertyGridManager)
Provides: perl(Wx::PropertyGridPage)
Provides: perl(Wx::PropertyInfo)
Provides: perl(Wx::PropertySheetDialog)
Provides: perl(Wx::RadioBox)
Provides: perl(Wx::RadioButton)
Provides: perl(Wx::RearrangeCtrl)
Provides: perl(Wx::RearrangeDialog)
Provides: perl(Wx::RearrangeList)
Provides: perl(Wx::Rect)
Provides: perl(Wx::RegConfig)
Provides: perl(Wx::Region)
Provides: perl(Wx::RegionIterator)
Provides: perl(Wx::Ribbon)
Provides: perl(Wx::RibbonArtProvider)
Provides: perl(Wx::RibbonAUIArtProvider)
Provides: perl(Wx::RibbonBar)
Provides: perl(Wx::RibbonBarEvent)
Provides: perl(Wx::RibbonButtonBar)
Provides: perl(Wx::RibbonButtonBarButtonBase)
Provides: perl(Wx::RibbonButtonBarEvent)
Provides: perl(Wx::RibbonControl)
Provides: perl(Wx::RibbonGallery)
Provides: perl(Wx::RibbonGalleryEvent)
Provides: perl(Wx::RibbonGalleryItem)
Provides: perl(Wx::RibbonMSWArtProvider)
Provides: perl(Wx::RibbonPage)
Provides: perl(Wx::RibbonPanel)
Provides: perl(Wx::RibbonToolBar)
Provides: perl(Wx::RibbonToolBarEvent)
Provides: perl(Wx::RibbonToolBarToolBase)
Provides: perl(Wx::RichText)
Provides: perl(Wx::RichTextAttr)
Provides: perl(Wx::RichTextBuffer)
Provides: perl(Wx::RichTextCharacterStyleDefinition)
Provides: perl(Wx::RichTextCtrl)
Provides: perl(Wx::RichTextEvent)
Provides: perl(Wx::RichTextFileHandler)
Provides: perl(Wx::RichTextFormattingDialog)
Provides: perl(Wx::RichTextHeaderFooterData)
Provides: perl(Wx::RichTextHTMLHandler)
Provides: perl(Wx::RichTextListStyleDefinition)
Provides: perl(Wx::RichTextParagraphStyleDefinition)
Provides: perl(Wx::RichTextPrinting)
Provides: perl(Wx::RichTextPrintout)
Provides: perl(Wx::RichTextRange)
Provides: perl(Wx::RichTextStyleComboCtrl)
Provides: perl(Wx::RichTextStyleDefinition)
Provides: perl(Wx::RichTextStyleListBox)
Provides: perl(Wx::RichTextStyleListCtrl)
Provides: perl(Wx::RichTextStyleOrganiserDialog)
Provides: perl(Wx::RichTextStyleSheet)
Provides: perl(Wx::RichTextXMLHandler)
Provides: perl(Wx::RichToolTip)
Provides: perl(Wx::SashEvent)
Provides: perl(Wx::SashWindow)
Provides: perl(Wx::ScreenDC)
Provides: perl(Wx::ScrollBar)
Provides: perl(Wx::ScrolledWindow)
Provides: perl(Wx::ScrollEvent)
Provides: perl(Wx::ScrollWinEvent)
Provides: perl(Wx::SearchCtrl)
Provides: perl(Wx::Server)
Provides: perl(Wx::SetCursorEvent)
Provides: perl(Wx::SettableHeaderColumn)
Provides: perl(Wx::SimpleHelpProvider)
Provides: perl(Wx::SimpleHtmlListBox)
Provides: perl(Wx::SingleChoiceDialog)
Provides: perl(Wx::SingleInstanceChecker)
Provides: perl(Wx::Size)
Provides: perl(Wx::SizeEvent)
Provides: perl(Wx::Sizer)
Provides: perl(Wx::SizerItem)
Provides: perl(Wx::Slider)
Provides: perl(Wx::SockAddress)
Provides: perl(Wx::SocketBase)
Provides: perl(Wx::SocketClient)
Provides: perl(Wx::SocketEvent)
Provides: perl(Wx::SocketServer)
Provides: perl(Wx::Sound)
Provides: perl(Wx::SpinButton)
Provides: perl(Wx::SpinCtrl)
Provides: perl(Wx::SpinCtrlDouble)
Provides: perl(Wx::SpinEvent)
Provides: perl(Wx::SplashScreen)
Provides: perl(Wx::SplitterEvent)
Provides: perl(Wx::SplitterWindow)
Provides: perl(Wx::StandardPaths)
Provides: perl(Wx::StaticBitmap)
Provides: perl(Wx::StaticBox)
Provides: perl(Wx::StaticBoxSizer)
Provides: perl(Wx::StaticLine)
Provides: perl(Wx::StaticText)
Provides: perl(Wx::StatusBar)
Provides: perl(Wx::StdDialogButtonSizer)
Provides: perl(Wx::StopWatch)
Provides: perl(Wx::Stream)
Provides: perl(Wx::StringProperty)
Provides: perl(Wx::StyledTextCtrl)
Provides: perl(Wx::StyledTextEvent)
Provides: perl(Wx::SVGFileDC)
Provides: perl(Wx::SymbolPickerDialog)
Provides: perl(Wx::SysColourChangedEvent)
Provides: perl(Wx::SystemColourProperty)
Provides: perl(Wx::SystemOptions)
Provides: perl(Wx::SystemSettings)
Provides: perl(Wx::TaskBarIcon)
Provides: perl(Wx::TaskBarIconEvent)
Provides: perl(Wx::TextAttr)
Provides: perl(Wx::TextAttrEx)
Provides: perl(Wx::TextCtrl)
Provides: perl(Wx::TextCtrlBase)
Provides: perl(Wx::TextCtrlIface)
Provides: perl(Wx::TextDataObject)
Provides: perl(Wx::TextDropTarget)
Provides: perl(Wx::TextEntry)
Provides: perl(Wx::TextEntryDialog)
Provides: perl(Wx::TextUrlEvent)
Provides: perl(Wx::TGAHandler)
Provides: perl(Wx::Thread)
Provides: perl(Wx::TIFFHandler)
Provides: perl(Wx::TimePickerCtrl)
Provides: perl(Wx::Timer)
Provides: perl(Wx::TimerEvent)
Provides: perl(Wx::TimeSpan)
Provides: perl(Wx::TipProvider)
Provides: perl(Wx::ToggleButton)
Provides: perl(Wx::ToolBar)
Provides: perl(Wx::ToolBarBase)
Provides: perl(Wx::ToolBarToolBase)
Provides: perl(Wx::Toolbook)
Provides: perl(Wx::ToolTip)
Provides: perl(Wx::TopLevelWindow)
Provides: perl(Wx::Treebook)
Provides: perl(Wx::TreebookEvent)
Provides: perl(Wx::TreeCtrl)
Provides: perl(Wx::TreeEvent)
Provides: perl(Wx::TreeItemData)
Provides: perl(Wx::TreeItemId)
Provides: perl(Wx::TreeListCtrl)
Provides: perl(Wx::TreeListEvent)
Provides: perl(Wx::TreeListItem)
Provides: perl(Wx::TreeListItemComparator)
Provides: perl(Wx::TypeInfo)
Provides: perl(Wx::UIActionSimulator)
Provides: perl(Wx::UIntProperty)
Provides: perl(Wx::UNIXaddress)
Provides: perl(Wx::UpdateUIEvent)
Provides: perl(Wx::URLDataObject)
Provides: perl(Wx::Validator)
Provides: perl(Wx::VarHScrollHelper)
Provides: perl(Wx::VarHVScrollHelper)
Provides: perl(Wx::Variant)
Provides: perl(Wx::VarScrollHelperBase)
Provides: perl(Wx::VarVScrollHelper)
Provides: perl(Wx::VideoMode)
Provides: perl(Wx::View)
Provides: perl(Wx::VListBox)
Provides: perl(Wx::VScrolledWindow)
Provides: perl(Wx::Wave)
Provides: perl(Wx::WebView)
Provides: perl(Wx::WebViewArchiveHandler)
Provides: perl(Wx::WebViewEvent)
Provides: perl(Wx::WebViewHandler)
Provides: perl(Wx::WebViewHistoryItem)
Provides: perl(Wx::Window)
Provides: perl(Wx::WindowCreateEvent)
Provides: perl(Wx::WindowDC)
Provides: perl(Wx::WindowDestroyEvent)
Provides: perl(Wx::WindowDisabler)
Provides: perl(Wx::WindowUpdateLocker)
Provides: perl(Wx::WinHelpController)
Provides: perl(Wx::Wizard)
Provides: perl(Wx::WizardEvent)
Provides: perl(Wx::WizardPage)
Provides: perl(Wx::WizardPageSimple)
Provides: perl(Wx::WrapSizer)
Provides: perl(Wx::XmlAttribute)
Provides: perl(Wx::XmlDocument)
Provides: perl(Wx::XmlNode)
Provides: perl(Wx::XmlProperty)
Provides: perl(Wx::XmlResource)
Provides: perl(Wx::XmlResourceHandler)
Provides: perl(Wx::XmlSubclassFactory)
Provides: perl(Wx::XPMHandler)
Provides: perl(Wx::ZipFSHandler)

%description
The Wx module is a wrapper for the wxWidgets (formerly known as
wxWindows) GUI toolkit.

This module comes with extensive documentation in HTML format;
you can download it from http://wxperl.sourceforge.net/.

%prep
%setup -q -n Wx-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

# Hooray for line ending differences.
dos2unix MANIFEST
dos2unix typemap

%patch -P3 -p1 -b .port

chmod -c a-x README.txt docs/todo.txt samples/*/*.pl
find . -type f -name "*.pm" -o -name "*.h" -o -name "*.cpp" |
    xargs chmod -c a-x


# OLD
%if 0
%filter_provides_in %{perl_vendorarch}/.*\\.so$ 
%filter_provides_in -P %{perl_archlib}/(?!CORE/libperl).*\\.so$ 
%filter_from_provides /perl(UNIVERSAL)/d; /perl(DB)/d 
%filter_from_provides /perl(Wx)$/d
%filter_from_provides /perl(MY)$/d
%filter_from_provides /perl(Parse::Yapp::Driver)/d
%filter_provides_in %{_docdir} 
%filter_requires_in %{_docdir} 
%filter_setup 
%endif

# NEW
%global __provides_exclude_from ^(%{perl_vendorarch}/.*\\.so)$
%global __provides_exclude ^perl\\((Wx|MY)\\)$
%{?perl_default_filter}


%build
perl Makefile.PL --wx-unicode \
  --wx-version=`wx-config --version | cut -d . -f 1-2` \
  --wx-toolkit=gtk \
  INSTALLDIRS=vendor \
  OPTIMIZE="$RPM_OPT_FLAGS -Wno-unused-variable -Wno-unused-but-set-variable -Wno-unused-local-typedefs"
make %{?_smp_mflags}

%install
make install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{?_with_testsuite:make test}

%files
%doc Changes README.txt docs/todo.txt wxpl.ico wxpl.xpm
%doc samples/
%{_bindir}/*
%{perl_vendorarch}/Wx*
%{perl_vendorarch}/auto/Wx/
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3pm*

%changelog
* Thu Jan 23 2025 Miro Hrončok <mhroncok@redhat.com> - 0.9932-38
- Rebuilt with perl(Alien::wxWidgets::Config::gtk_3_2_6_uni_gcc_3_4)
- Fixes: rhbz#2341695

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9932-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9932-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Miro Hrončok <mhroncok@redhat.com> - 0.9932-35
- Rebuilt with perl(Alien::wxWidgets::Config::gtk_3_2_5_uni_gcc_3_4)
- Fixes: rhbz#2292728

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.9932-34
- Perl 5.40 rebuild

* Tue Jan 30 2024 Tom Callaway <spot@fedoraproject.org> - 0.9932-33
- use new filtering macros
- fix license tag
- add explicit requires on perl(Alien::wxWidgets::Config::gtk_XXX) that we build against

* Tue Jan 30 2024 Miro Hrončok <mhroncok@redhat.com> - 0.9932-32
- Rebuilt with perl(Alien::wxWidgets::Config::gtk_3_2_4_uni_gcc_3_4)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9932-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9932-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9932-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.9932-28
- Perl 5.38 rebuild

* Fri Jan 20 2023 Scott Talbert <swt@techie.net> - 0.9932-27
- Rebuild with wxWidgets 3.2

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9932-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9932-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.9932-24
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9932-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9932-22
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.9932-21
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9932-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9932-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.9932-18
- Perl 5.32 rebuild

* Mon Mar 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.9932-17
- Specify all dependencies

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9932-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9932-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.9932-14
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9932-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 22 2018 Scott Talbert <swt@techie.net> - 0.9932-12
- Rebuild with wxWidgets 3.0

* Mon Jul 23 2018 Tom Callaway <spot@fedoraproject.org> - 0.9932-11
- add BuildRequires: gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9932-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.9932-9
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9932-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9932-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9932-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.9932-5
- Rebuild due to bug in RPM (RHBZ #1468476)

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.9932-4
- Perl 5.26 re-rebuild of bootstrapped packages

* Wed Jun 07 2017 Petr Pisar <ppisar@redhat.com> - 0.9932-3
- Work around BOM_UTF8 clash between wxGTK and Perl (CPAN RT#121464)

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.9932-2
- Perl 5.26 rebuild

* Tue Apr 18 2017 Tom Callaway <spot@fedoraproject.org> - 0.9932-1
- update to 0.9932

* Mon Apr 17 2017 Tom Callaway <spot@fedoraproject.org> - 0.9931-1
- update to 0.9931

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9928-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.9928-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9928-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Tom Callaway <spot@fedoraproject.org> - 0.9928-1
- update to 0.9928

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9927-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.9927-3
- Perl 5.22 rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9927-2
- Rebuilt for GCC 5 C++11 ABI change

* Fri Mar 27 2015 Tom Callaway <spot@fedoraproject.org> - 0.9927-1
- update to 0.9927

* Fri Mar 13 2015 Tom Callaway <spot@fedoraproject.org> - 0.9926-1
- update to 0.9926

* Wed Feb 25 2015 Petr Pisar <ppisar@redhat.com> - 0.9923-3
- Rebuild for reverted GCC 5.0 C++ ABI signature

* Thu Feb 12 2015 Petr Pisar <ppisar@redhat.com> - 0.9923-2
- Rebuild for new GCC 5.0 C++ ABI signature (bug #1190971)

* Wed Feb  4 2015 Tom Callaway <spot@fedoraproject.org> - 0.9923-1
- update to 0.9923
- comment out pass_through option to Getopt-Long (not valid with <>)

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.9922-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9922-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9922-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 17 2014 Miro Hrončok <mhroncok@redhat.com> - 0.9922-1
- Update to 0.9922 (#958819)
- No longer BR perl(ExtUtils::XSpp) >= 0.1602 (#1077413)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9921-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.9921-2
- Perl 5.18 rebuild

* Wed Apr 17 2013 Tom Callaway <spot@fedoraproject.org> - 0.9921-1
- update to 0.9921

* Thu Apr  4 2013 Tom Callaway <spot@fedoraproject.org> - 0.9918-1
- update to 0.9918

* Tue Feb 12 2013 Tom Callaway <spot@fedoraproject.org> - 0.9917-1
- update to 0.9917

* Sun Jan 20 2013 Tom Callaway <spot@fedoraproject.org> - 0.9916-1
- update to 0.9916

* Wed Jan  2 2013 Tom Callaway <spot@fedoraproject.org> - 0.9915-1
- update to 0.9915

* Thu Nov 15 2012 Tom Callaway <spot@fedoraproject.org> - 0.9914-2
- fix provides to be more complete

* Mon Oct  8 2012 Tom Callaway <spot@fedoraproject.org> - 0.9914-1
- update to 0.9914

* Mon Oct  1 2012 Tom Callaway <spot@fedoraproject.org> - 0.9913-1
- update to 0.9913

* Fri Aug 24 2012 Tom Callaway <spot@fedoraproject.org> - 0.9911-1
- update to 0.9911

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9907-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.9907-2
- Perl 5.16 rebuild

* Fri May 11 2012 Tom Callaway <spot@fedoraproject.org> - 0.9907-1
- update to 0.9907

* Tue Apr  3 2012 Tom Callaway <spot@fedoraproject.org> - 0.9906-1
- update to 0.9906

* Wed Mar 21 2012 Tom Callaway <spot@fedoraproject.org> - 0.9905-1
- update to 0.9905

* Fri Mar  2 2012 Tom Callaway <spot@fedoraproject.org> - 0.9904-1
- update to 0.9904

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9903-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Tom Callaway <spot@fedoraproject.org> - 0.9903-1
- update to 0.9903

* Thu Oct 20 2011 Tom Callaway <spot@fedoraproject.org> - 0.9902-1
- update to 0.9902

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.9901-2
- Perl mass rebuild

* Tue Jun  7 2011 Tom Callaway <spot@fedoraproject.org> - 0.9901-1
- update to 0.9901

* Mon May  9 2011 Tom Callaway <spot@fedoraproject.org> - 0.99-1
- update to 0.99

* Wed Feb  9 2011 Tom Callaway <spot@fedoraproject.org> - 0.98-5
- add explicit provides for all XS files, not just the ones in XS/

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb  8 2011 Tom Callaway <spot@fedoraproject.org> - 0.98-3
- add explicit provides for the stuff in the XS/ directory that
  isn't autodetected

* Thu Jan 27 2011 Tom Callaway <spot@fedoraproject.org> - 0.98-2
- update filtering macros, filter out requires on Wx::PlValidator

* Wed Jan 26 2011 Tom Callaway <spot@fedoraproject.org> - 0.98-1
- update to 0.98

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.92-5
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 0.92-4
- rebuilt against wxGTK-2.8.11-2

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.92-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.92-2
- rebuild against perl 5.10.1

* Sat Sep  5 2009 Stepan Kasal <skasal@redhat.com> - 0.92-1
- new upstream version

* Thu Aug 20 2009 Stepan Kasal <skasal@redhat.com> - 0.91-8
- rebuild with perl-Alien-wxWidgets-0.44-2

* Thu Aug 20 2009 Stepan Kasal <skasal@redhat.com> - 0.91-7
- rebuild against patched perl-Alien-wxWidgets

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul  7 2009 Stepan Kasal <skasal@redhat.com> - 0.91-5
- return back RPM_OPT_FLAGS

* Tue Jul  7 2009 Stepan Kasal <skasal@redhat.com> - 0.91-4
- rebuild against perl-5.10.0-72 (#508496)

* Mon Jun 29 2009 Marcela Mašláňová <mmaslano@redhat.com> - 0.91-3
- remove RPM_OPT_FLAGS which create message: undefined symbol: Perl_Guse_safe_putenv_ptr
- Resolves: rhbz#508496

* Fri Jun 19 2009 Stepan Kasal <skasal@redhat.com> - 0.91-2
- rebuild

* Wed Jun  3 2009 Marcela Mašláňová <mmaslano@redhat.com> - 0.91-1
- update

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.89-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.89-1
- 0.89

* Tue Mar  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.81-1
- 0.81
- minor packaging cleanups

* Tue Mar  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.80-4
- rebuild for new perl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.80-3
- Autorebuild for GCC 4.3

* Fri Nov 30 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.80-2
- fix bogus requires

* Wed Nov 28 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.80-1
- bump to 0.80

* Thu Jun  7 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.74-1
- Update to 0.74.

* Sun Apr 22 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.73-1
- Update to 0.73.

* Sun Apr  1 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.72-1
- Update to 0.72.

* Sat Mar 31 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.71-1
- Update to 0.71.

* Fri Mar 23 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.70-1
- Update to 0.70.

* Sun Mar 18 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.69-1
- Update to 0.69.

* Thu Jan 25 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.67-2
- Filtering out perl(Parse::Yapp::Driver) from the provides list (#224238).
- Filtering out perl(MY) from the provides list.

* Sat Dec 16 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.67-1
- Update to 0.67.

* Sat Dec 16 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.66-1
- Update to 0.66.

* Fri Dec 15 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.65-2
- Rebuild (wxGTK 2.8.0).

* Thu Dec  7 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.65-1
- Update to 0.65.

* Fri Dec  1 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.64-1
- Update to 0.64.

* Wed Nov 22 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.63-1
- Update to 0.63.

* Tue Nov 14 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.62-1
- Update to 0.62.

* Sat Nov 11 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.60-1
- Update to 0.60.

* Sat Oct 21 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.59-1
- Update to 0.59.

* Fri Oct 20 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.58-1
- Update to 0.58.

* Sun Oct  1 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.57-2
- Filtered perl(Wx) duplicate provide.
- Corrected several file permission.

* Sun Sep 24 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.57-1
- Update to 0.57.

* Sun May 14 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.27-1
- First build.
