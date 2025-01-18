Name:           fonts-compare
Version:        1.5.4
Release:        2%{?dist}
Summary:        Tool to compare fonts for a language

License:        GPL-2.0-or-later
URL:            https://github.com/sudipshil9862/fonts-compare
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/fonts-compare-%{version}.tar.gz

BuildArch: noarch

BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel 
Requires: python3-gobject
Requires: python3-langtable
Requires: python3-langdetect
Requires: fontconfig
Requires: hicolor-icon-theme
Requires: gtk4
Requires: python3-freetype
Requires: libadwaita

%description
Fonts-Compare is a tool that enables individuals
to compare various fonts in a particular language.



%prep
%autosetup


%build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}/
install -D -m 755 fonts-compare %{buildroot}%{_bindir}/%{name}
install -D -m 755 fonts_compare.py %{buildroot}%{_datadir}/%{name}/
install -m 644 -D org.github.sudipshil9862.fonts-compare.desktop %{buildroot}/%{_datadir}/applications/org.github.sudipshil9862.%{name}.desktop
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps/
install -D -m 644 logo/16x16/fonts-compare.png %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps/
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/22x22/apps/
install -D -m 644 logo/22x22/fonts-compare.png %{buildroot}/%{_datadir}/icons/hicolor/22x22/apps/
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
install -D -m 644 logo/32x32/fonts-compare.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/
install -D -m 644 logo/48x48/fonts-compare.png %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/
install -D -m 644 logo/64x64/fonts-compare.png %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/
install -D -m 644 logo/128x128/fonts-compare.png %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/
install -D -m 644 logo/256x256/fonts-compare.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/
mkdir -p %{buildroot}/usr/share/icons/hicolor/scalable/apps/
install -D -m 644 logo/fonts-compare.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.github.sudipshil9862.%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/org.github.sudipshil9862.%{name}.desktop
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/16x16/
%dir %{_datadir}/icons/hicolor/22x22/
%dir %{_datadir}/icons/hicolor/32x32/
%dir %{_datadir}/icons/hicolor/48x48/
%dir %{_datadir}/icons/hicolor/64x64/
%dir %{_datadir}/icons/hicolor/128x128/
%dir %{_datadir}/icons/hicolor/256x256/
%dir %{_datadir}/icons/hicolor/scalable/
%dir %{_datadir}/icons/hicolor/scalable/apps/
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jan 06 2025 Sudip Shil <sshil@redhat.com> - 1.5.4-1
- Started porting fonts-compare to use libadwaita on top of GTK for a modern and responsive UI.
- Refactored CustomDialog to enhance usability.
- Fontname of fontbutton has normal fontweight and removed bold weight from name of button.
- Enhanced language detected language to appear at the top of the language list after text detection in the Edit Label button.

* Tue Oct 22 2024 Sudip Shil <sshil@redhat.com> - 1.5.3-1
- Fixed: First font button selects a font even when no fonts are installed.
- Returns the language name if no Pango sample text is available for the language.
- Added support for RHEL ZhongYi Song fonts and fonts with special characters like //-.
- Font button font list and font size now support RHEL ZhongYi Song fonts.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 13 2024 Sudip Shil <sshil@redhat.com> - 1.5.2-2
- deleted tarball from files

* Wed Jun 12 2024 Sudip Shil <sshil@redhat.com> - 1.5.2-1
- Fixed an error caused by changes to the font button and sample text, discovered with Urdu and several other languages.
- Updated the About section to include version and license information.
- Renamed "label" to "text".
- bugfix: added libadwaita dependency

* Wed May 8 2024 Sudip Shil <sshil@redhat.com> - 1.5.1-1
- New Feature: Initialize fonts-compare with locale
- --lang feature handles zh-cn and zh_CN both format
- Any valid locale, unknown to fontconfig will fallback to en/C.utf8
- Any unsupported locale, fallback to C.utf8
- Language variable handling to support both LC_ALL and LANG settings

* Thu May 2 2024 Sudip Shil <sshil@redhat.com> - 1.5.0-1
- Initialize fonts-compare with language from cli "fonts-compare --lang ja"
- Now user can turn off the Auto language detection for their words in edit label
- Now both buttons select different fonts. They will not select similar/same font
- fixed issue auto langdetect changing fonts for both fontbutton
- activate dark theme if system's dark mode is enabled, used libadwaita
- Avoiding the fontconfig limitation with locales like - Choosing -* giving same font
- droid fonts will never be selected
- changed README

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 24 2023 Sudip Shil <sshil@redhat.com> - 1.4.0-3
- removed unnecessary dependency

* Wed Aug 23 2023 Sudip Shil <sshil@redhat.com> - 1.4.0-2
- removed some pylint errors and cleaned logs

* Mon Aug 21 2023 Sudip Shil <sshil@redhat.com> - 1.4.0-1
- get fontversion for a font that is selected. python3-freetype will be used for this.
- fontversion update upon language change from drop-down and alsofont change in each fontbutton
- the style/weight is hide by default. added option to show style
- show-style and fontversion feature won't be available in f37
- font filter for rawhide is fast now and fonts are now fast to populate
- Set activate on single click to false for the language selection listbox
- fixed indexing bug: Clicking arabic language in drop-down selects assamese
- now fontsize adjustment will work
- fixed non printable string getting from freetype function
- removed classmethod and added instance method for label_font_change_newversion
- noto sans won't appear as noto sans regular
- gtk.dialog deprecation warning issue fixed
- dialog button bug of fontbutton2 fixed
- added run.sh script
- fonts-compare will work on rhel9
- Selecting second font from fc-list for second font button

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 27 2023 Sudip Shil <sshil@redhat.com> - 1.3.2-1
- gtk4 dependency added
- --help text added

* Tue Apr 11 2023 Sudip Shil <sshil@redhat.com> - 1.3.1-3
- changelog fixing

* Tue Apr 11 2023 Sudip Shil <sshil@redhat.com> - 1.3.1-2
- LICENSE changed to GPL-2.0-or-later
- removed unnecessary directory that created by spec

* Tue Apr 11 2023 Sudip Shil <sshil@redhat.com> - 1.3.1-1
- LICENSE changed to GPL-2.0+
- little change in README

* Wed Apr 5 2023 Sudip Shil <sshil@redhat.com> - 1.3.0-1
- licence update with MIT
- some core spec file issues fixed and updated
- Package must own all directories that it creates, this issue fixed
- README.md update with instruction and commands

* Thu Mar 30 2023 Sudip Shil <sshil@redhat.com> - 1.2.7-1
- spec file updated
- fixed issue: wrong-icon-size errors raised by the fedora-review

* Thu Mar 30 2023 Sudip Shil <sshil@redhat.com> - 1.2.6-2
- spec file updated

* Wed Mar 29 2023 Sudip Shil <sshil@redhat.com> - 1.2.6-1
- more information in README.md
- some code rendering and bux fixed

* Mon Mar 20 2023 Sudip Shil <sshil@redhat.com> - 1.2.5-1
- dealing with unscalable fonts like Fixed, Biwidth
- dealing with fonts with PCF fontformat
- resolves Fontbutton shoes None
- Fonts of which languages are not installed in your system with a command: python3 fonts_compare.py --nofonts
- resolves reopen issue: https://github.com/sudipshil9862/fonts-compare/issues/33
- resolves: https://github.com/sudipshil9862/fonts-compare/issues/34

* Thu Mar 9 2023 Sudip Shil <sshil@redhat.com> - 1.2.4-1
- Resolves: https://github.com/sudipshil9862/fonts-compare/issues/33

* Fri Mar 3 2023 Sudip Shil <sshil@redhat.com> - 1.2.3-1
- Resolves: FontButton displays 'None'. https://github.com/sudipshil9862/fonts-compare/issues/32 
- bug fixed generated by filtering-fonts for above gtk-version-4.9 users

* Mon Feb 27 2023 Sudip Shil <sshil@redhat.com> - 1.2.2-1
- Resolves: https://github.com/sudipshil9862/fonts-compare/issues/31

* Wed Feb 22 2023 Sudip Shil <sshil@redhat.com> - 1.2.1-1
- merged code which supports all OS
- supports gtk verison below 4.9 and above 4.9

* Mon Feb 20 2023 Sudip Shil <sshil@redhat.com> - 1.2.0-1
- Resolves: https://github.com/sudipshil9862/fonts-compare/issues/25
- Resolves: https://github.com/sudipshil9862/fonts-compare/issues/26
- Resolves: https://github.com/sudipshil9862/fonts-compare/issues/27
- Resolves: https://github.com/sudipshil9862/fonts-compare/issues/28
- after entrybox text changed in gtkdialog, pressing enter will trigger OK signal
- font labels only have the FAMILY now, style not required
- made wrap toggle and wrapping of lebels are better than previous version
- filtering fonts for specific language solved
- make language search more clever
- now more accuarate indic languages search in language search drop-down
- selected language will be shown above all languages in language search drop-down and delete malayalam, urdu screenshot
- dark theme added
- If font_size changed then window_size will reset
- search entry focused in initialization
- version tag remove from desktop file
- all mypy errors solved
- code rendering
- ui menu screenshot updated
- logo changed made by inkscape

* Fri Jan 27 2023 Sudip Shil <sshil@redhat.com> - 1.1.4-1
- Add desktop-validation for org.github.sudipshil9862.fonts-compare.desktop
- made language search more clever, more selective in language search drop down
- more accuarate indic languages search
- selected language will be shown above all languages in language search drop-down
- made layout more size responsive
- logo changed made by inkscape
- search entry focused in initialization of program
- dark theme added
- updated all indic languages screenshots with pango sample texts of fonts-compare UI in https://sshil.fedorapeople.org/lohit-vs-noto-comparison.html

* Fri Jan 6 2023 Sudip Shil <sshil@redhat.com> - 1.1.3-1
- Changed Application ID
- Renamed desktop entry file name

* Thu Jan 5 2023 Sudip Shil <sshil@redhat.com> - 1.1.2-1
- changed logo for fonts-compare

* Thu Jan 5 2023 Sudip Shil <sshil@redhat.com> - 1.1.1-1
- spec file updated with installing svg
 
* Thu Jan 5 2023 Sudip Shil <sshil@redhat.com> - 1.1.0-1
- Desktop entry file added
- fonts-compare logo created
- README file updated
- Some name changes in UI

* Mon Jan 2 2023 Sudip Shil <sshil@redhat.com> - 1.0.9-1
- Added custom dialog in edit label menu button to edit labels by entry textbox, added langdetect label, buttons borders removed, code changes with class inheritance
- Edit labels from entry and labels will be changed, language detection for text that being typed in entry textbox, ok and cancel button functions fixed
- Solved major pylint errors
- Font size adjustment widget and spin button font size adjustment widget both widgets shifted to hamburger menu, title name changed
- pango sample text checkboxadded in menu
- Now code selects only font fc-list and won't select Family+Style, fontbutton selects style by-default, code rendering, remove unused horizontal boxes
- Added fallback checkbox in menu
- Dropped language label full name that shows up in main ui, instead used tooltip/hover over language selector
- Removed glibx XX_YY locals from language list
- code rendering, reduced spaces, reduced vertical and hotizontal boxes used, font adjustment bug fixed
- fonts compare's screenshots added in readme file and https://sshil.fedorapeople.org/lohit-vs-noto-comparison.html

* Wed Dec 14 2022 Sudip Shil <sshil@redhat.com> - 1.0.8-1
- Bug fixed: No text shows up if langtable sample text selected after selecting pango sample text

* Wed Dec 14 2022 Sudip Shil <sshil@redhat.com> - 1.0.7-1
- Added header bar, hamburger menu
- Added searchable language widget
- About, quit button in hamburger menu
- Solved issue with fc-match (like bn_IN, bn_Bd not recognizable by fc-match)
- Sometimes random_font doesnot contain any style then error arises fixed
- Added spin adjustment button to increase decrease of fontsize of labels
- Highlighting the error if fonts not installed instead of dialog box
- Use pango sample text inside hamburger toggle button
- font slider removed
- vertical and horizontal boxes adjustment done
- python language list removed for this release
- Wrap text above fontsize 50 for text labels
- Fixed header bar bugs

* Thu Dec 1 2022 Sudip Shil <sshil@redhat.com> - 1.0.6-1
- Dictionary removed
- Attempt language detection only when the entered text really changed
- added toggle button for Pango and Langtable sample text
- set langtable sample text as default when toggle switch is off 
- Blocking entry function's signal for some time so that it avoids language detection again
- Availability of languages from langtable, fontconfig and python
- label text added for showing the error if no font is installed for a language
- HId error label when fonts of any language actually are installed
- dialog box code removed
- default sample string by langtable, global variables removed, some global functions removed
- text wrapping and removed unnecessary code
- some vertical and horizontal boxes bug fixed
- fixed pylint warnings
- added missing type hints

* Mon Nov 14 2022 Sudip Shil <sshil@redhat.com> - 1.0.5-1
- random font generator for second text
- Instruction to debug and installing new fonts for different languages added in README.md file
- All languages supported
- ui design changed

* Mon Oct 31 2022 Sudip Shil <sshil@redhat.com> - 1.0.4-1
- font slider added, more languages added, more fonts supported, README file as user manual

* Tue Oct 18 2022 Sudip Shil <sshil@redhat.com> - 1.0.3-1
- fixed broken macros
- on_changed function deactivated for a while added

* Sun Oct 16 2022 Sudip Shil <sshil@redhat.com> - 1.0.2-1
- updated version 1.0.2-1
- Bug 1 fixed: errors and warning removed - checked pylint, 
  pylintrc parameters updated for this project specificly
- Bug 2 fixed: If I type japanese text in gtkEntry then no font detected in font button
  https://github.com/sudipshil9862/fonts-compare/issues/3
- Bug 3 fixed: If click ‘bn’ then font button dialog has bengali text below 
  but not happening this for ‘ja’ -> showing some english text instead of japanese 
  https://github.com/sudipshil9862/fonts-compare/issues/2
- Bug 4 fixed: If I write japanese in gtkEntry field and then I select ‘bn’ from drop then everything changed 
  but the japanese text still there in gtkEntry
- Bug 5 fixed: When a language is detected by typing a text, 
  the combobox(drop-down) doesn’t change
  https://github.com/sudipshil9862/fonts-compare/issues/5
- Bug 6 fixed: code_rendering - detecting combo box lang using for loop and making it general 
  so that any language can be selected from drop-down if it’s there  (use dictionary)
- Bug 7 fixed: Text in the entry suddenly changes to sample text 
  for the detected language when typing into the entry
  https://github.com/sudipshil9862/fonts-compare/issues/6

* Tue Sep 27 2022 Sudip Shil <sshil@redhat.com> - 1.0.1-1
- updated version 1.0.1-1

* Fri Sep 23 2022 Sudip Shil <sshil@redhat.com> - 1.0.0-1
- Initial RPM release
