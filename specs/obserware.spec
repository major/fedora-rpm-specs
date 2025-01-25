%global uuid org.t0xic0der.obserware

Name:           obserware
Version:        0.2.10
Release:        1%{?dist}
Summary:        An advanced system monitor utility written in Python and Qt

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Url:            https://gitlab.com/t0xic0der/%{name}
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel

%description
An advanced system monitor utility written in Python and Qt

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}
mkdir -p %{buildroot}%{_datadir}/applications %{buildroot}%{_metainfodir} %{buildroot}%{_datadir}/pixmaps
cp %{buildroot}%{python3_sitelib}/%{name}/appdata/%{uuid}.desktop %{buildroot}%{_datadir}/applications/%{uuid}.desktop
cp %{buildroot}%{python3_sitelib}/%{name}/appdata/%{uuid}.metainfo.xml %{buildroot}%{_metainfodir}/%{uuid}.metainfo.xml
cp %{buildroot}%{python3_sitelib}/%{name}/appdata/%{uuid}.png %{buildroot}%{_datadir}/pixmaps/%{uuid}.png

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{uuid}.desktop
appstream-util validate-relax --nonet %{buildroot}%{python3_sitelib}/%{name}/appdata/%{uuid}.metainfo.xml

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_metainfodir}/%{uuid}.metainfo.xml
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/pixmaps/%{uuid}.png

%changelog
* Thu Jan 23 2025 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.2.10-1
- Attempt fixing FTI https://bugzilla.redhat.com/show_bug.cgi?id=2341694

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.9-12
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.9-10
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 0.2.9-6
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 18 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 0.2.9-4
- Rebuild for python and updated py deps (fixes RHBZ#2137855)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.2.9-2
- Rebuilt for Python 3.11

* Sat Feb 19 2022 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.2.9-1
- v0.2.9 - Released on February 19th, 2022
- Find the release here - https://gitlab.com/t0xic0der/obserware/-/releases/v0.2.9
- Updated Flatpak manifest files according to the updated version tag
- Removed the CPU cycles dialog box and the CPU cycles widget list items
- Removed the CPU times dialog box and the CPU times widget list items
- Removed the dedicated information provider for the CPU cycles and CPU times
- Redesigned the performance widget list item to include both CPU cycles and CPU times
- Added a performance tabscreen with widget listing for CPU cycles and CPU times
- Moved the static CPU information from the information tabscreen to the new tabscreen
- Transferred the information provider under the tabscreen hierarchy
- Redesigned the information tabscreen to accommodate the limited set of static info
- Cleaned up the source code and UI assets for needless UI elements
- Reorganized the mainwind operations' methods for better code readability
- Fixed the bug where the widget list would scroll back to the top on refresh
- Added a manual refresh button in the network tabscreen and partitions tabscreen
- Addressed exceptions by logging events of network devices or partitions changes
- Changed cursor into a pointing hand when hovering over buttons in the per-process dialog
- Optimized imports involving PyQt5 for consistency and better code readability
- Added a new status bar at the bottom to express more information about operations
- Offloaded logging information interactively to the status bar about manual refreshes
- Offloaded logging information interactively to the status bar about device changes
- Offloaded logging information interactively to the status bar about process interactions
- Reworked methods involving logging to print log texts and return logging strings
- Handled exception when obtaining info of a visibly listed but non-existent process
- Updated the lock file to keep up with the recent versions of the dependencies
- Updated the documentation and the metainfo files with the most recent screenshots
- Fixed the newly added screenshot references in the documentation
- Fixed the selectability of the elements in the CPU list of the performance tabscreen

* Sun Jan 30 2022 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.2.8-1
- v0.2.8 - Released on January 30th, 2022
- Find the release here - https://gitlab.com/t0xic0der/obserware/-/releases/v0.2.8
- Fixed crashes when certain CPU specifications parameters were requested for but were not available
- Fixed crashes when certain CPU features parameters were requested for but were not available
- Added `Flake8`, `Pytest`, `Pytest-Black`, `Pytest-Isort` and `Pytest-Flake8` as development dependencies
- Enhanced contributor experience with `Black`, `Isort` and `Flake8` formatted source code
- Reworked project specification to allow for `Black`, `Isort` and `Flake8` code checks, locally and on CI
- Added `xmllint` checks for application metainfo file as a CI directive
- Replaced multistep code quality check with `Pytest` mediated `Black`, `Isort` and `Flake8` code checks
- Updated copyright year in source code files, application metainfo files, CI directive file and interface
- Added a new tabscreen for showing storage counters, physical partitions and logical partitions
- Added combined statistics reader for the storage counters, physical partitions and logical partitions
- Removed dedicated dialog box for storage counters and moved the metrics to the newly added tabscreen
- Removed dedicated dialog box for physical partitions and moved the metrics to the newly added tabscreen
- Removed dedicated dialog box for logical partitions and moved the metrics to the newly added tabscreen
- Removed segregated statistics readers for the storage counters, physical partitions and logical partitions
- Deprecated reading of busy time on storage counter statistics
- Deprecated reading of maximum filename length and maximum pathname length on physical partitions statistics
- Deprecated reading of maximum filename length and maximum pathname length on logical partitions statistics
- Reworked widgets for listing of physical partitions and logical partitions on the newly added tabscreen
- Removed extra width from the right side of the widgets for the network devices listing
- Reworked placeholder/dynamic units for use in displaying file sizes and network speeds correctly
- Resize application icon to meet Flatpak requirements
- Added manifests and helper files to provision distribution as a Flatpak package

* Thu Jan 20 2022 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.2.7-1
- v0.2.7 - Released on January 20th, 2022
- Find the release here - https://gitlab.com/t0xic0der/obserware/-/releases/v0.2.7
- Switched fontface for header/statistic elements from JetBrains Mono to Barlow Sans
- Phased out default colours in favour of a better support for the global system-wide theming
- Iconified the activity state of the per-NIC listing item for better graphical representation
- Reduced the sizes of the dialog boxes and widget items to save space on changed fontface
- Added a new CI test directive to check for the validity of the Qt UI files
- Set application style to `Fusion` for graphical consistency across desktop environments
- Fixed crashes from `ZeroDivisionError` on environments where no swap partitions are present
- Fixed graphical artifacts for the icon elements on the widget display of network statistics
- Modularized size formatting function for use in physical and logical partitions and network readers
- Added size formatting in the physical and virtual memory display of the main screen
- Added size formatting in the CPU frequency listing display of the CPU Cycles dialog box
- Added size formatting in the times display of the CPU Times dialog box
- Added size formatting in the statistics display of the Storage Statistics dialog box
- Included support for Python 3.8, 3.9, 3.10 and 3.11 by adding the respective trove classifiers
- Updated the documentation with newer screenshots for the recent release

* Fri Jan 07 2022 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.2.6-1
- v0.2.6 - Released on January 07th, 2022
- Find the release here - https://gitlab.com/t0xic0der/obserware/-/releases/v0.2.6
- Added Font Awesome 5 fontface assets to the project
- Added tabscreen view for the network statistics with widget listing
- Added combined reader for the network statistics tabscreen view
- Removed dialog box for the network statistics with tabular view
- Removed standalone reader for the network statistics dialog box
- Fixed highlight color for the `QListWidget` elements on the information tabscreen
- Fixed highlight color for the `QTableWidget` rows on the process tabscreen
- Stepped down the Python version requirement from Python 3.10 to Python 3.8
- Moved icon imports from static image assets to Font Awesome 5 fontface assets
- Removed useless static image assets, resource bytecodes and XML references
- Restored list item highlighting according to the application theme
- Added GitLab CI pipeline configuration file for checking code quality and build state
- Formatted the source code and sorted the dependency imports
- Removed border radius from frames, progress bars and buttons
- Set the vertical scrollbars for the dialog boxes to be always visible
- Used `PyQt5.QtCore.qVersion` instead of `PyQt5.Qt.PYQT_VERSION_STR`
- Updated the documentation with newer screenshots for the recent release

* Thu Dec 30 2021 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.2.5-1
- v0.2.5 - Released on December 30th, 2021
- Find the release here - https://gitlab.com/t0xic0der/obserware/-/releases/v0.2.5
- Restructured the source code into a cascading layout
- Removed tabular listing of logical partitions in the logical partitions dialog box
- Added a widget-wise listing of the logical partitions in the logical partitions dialog box
- Included storage occupancy display with the use of `QProgressBar` element for each partition
- Added permalink of the screenshots on the project documentation
- Fixed variable names of the widget subclass of the physical partitions dialog box
- Transferred UI assets like fonts, images, UI files and resources to the parent directory
- Updated the documentation with newer screenshots for the recent release
- Worked on the distribution of Obserware as a standard desktop application
- Fixed the relative location of Logical Partitions widget UI file on the project storage
- Made the application available for installation/usage on Fedora COPR and Flathub

* Sun Dec 26 2021 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.2.4-1
- v0.2.4 - Released on December 26th, 2021
- Find the release here - https://gitlab.com/t0xic0der/obserware/-/releases/v0.2.4
- Increased project visibility by adding a featured section to README.md
- Corrected maximum dimensions of the CPU Cycles dialog box
- Removed tabular listing of physical partitions in the physical partitions dialog box
- Added a widget-wise listing of the physical partitions in the physical partitions dialog box
- Included storage occupancy display with the use of `QProgressBar` element for each partition
- Reworked main window to comply with the global system colour scheme in Qt-based desktop environments
- Reworked CPU Cycles dialog box to comply with the global system colour scheme in Qt-based desktop environments
- Reworked CPU Times dialog box to comply with the global system colour scheme in Qt-based desktop environments
- Reworked Storage Counters dialog box to comply with the global system colour scheme in Qt-based desktop environments
- Reworked Network Statistics dialog box to comply with the global system colour scheme in Qt-based desktop environments
- Reworked Process Statistics dialog box to comply with the global system colour scheme in Qt-based desktop environments
- Reworked Physical Partitions dialog box to comply with the global system colour scheme in Qt-based desktop environments
- Reworked Logical Partitions dialog box to comply with the global system colour scheme in Qt-based desktop environments
- Fixed the physical partitions dialog header to be in title-case
- Updated the documentation with newer screenshots for the recent release

* Wed Dec 15 2021 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.2.3-1
- v0.2.3 - Released on December 15th, 2021
- Find the release here - https://gitlab.com/t0xic0der/obserware/-/releases/v0.2.3
- Redesigned CPU times dialog box to better describe the purpose
- Added widget block and widget list interfaces for CPU times
- Restructured provider module schema to be more semantic
- Made the window to be initialized on center of the screen
- Updated documentation to mark recent release of the current version
- Hard-coded font styles to make it agnostic to system font styling in UI assets
- Hard-coded font styles to make it agnostic to system font styling in interface modules
- Set uniform row heights on `QTableWidget` elements used to display network devices listing
- Set uniform row heights on `QTableWidget` elements used to display physical partitions listing
- Set uniform row heights on `QTableWidget` elements used to display logical partitions listing
- Allowed for uniform scaling in accordance with the global scaling factor

* Sat Dec 04 2021 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.2.2-1
- v0.2.2 - Released on December 4th, 2021
- Find the release here - https://gitlab.com/t0xic0der/obserware/-/releases/v0.2.2
- Added detailed graphical view for per-core CPU usage and frequency statistics
- Nested CPU times dialog box inside of CPU cycles dialog box
- Added Gitignore file configured for Python projects
- Updated documentation to mark recent release of the current version

* Fri Dec 03 2021 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.2.1-1
- v0.2.1 - Released on December 3rd, 2021
- Find the release here - https://gitlab.com/t0xic0der/obserware/-/releases/v0.2.1
- Initialized the project
- Added interactive quick-access bottombar for easy statistics
- Added graphical landing view for CPU, memory and swap statistics in the Performance section
- Added tabular process listing view in the Processes section
- Added CPU times tabular view in the CPU times dialog box
- Added storage counter view in the storage counter dialog box
- Fixed naming on the header for storage counters dialog box
- Fixed CPU count display information from the provider
- Added tabular partition listing view in the physical and logical partitions dialog boxes
- Added per-process statistics view in the per-process dialog box
- Had project licensed under GPL 3.0 or later
- Added network statistics view in the network statistics dialog box
- Fixed height of the storage counters dialog box
- Added static information view for software and specifications in the Information section
- Fixed retrieval of useless static data for the landing view
- Fixed time format in the per-process statistics view dialog box
- Mutated all child windows to dialog boxes
- Fixed inheritance in dialog boxes for automatically centering them
- Fixed action references to non-existent processes
- Added warning level logging for operations on process interaction
- Added contributing view for attributions and license information
- Extended project documentation with screenshots and usage information
- Fixed additional rows on table views for CPU times, logical partitions, physical partitions, network statistics and process listing
- Marked first public release for current release and updated documentation
- Fixed broken references to included fonts in the application
- Fixed addition of font resources asset and performed version bump
