%if 0%{?rhel} == 8
%define anaconda_core_version 33
%endif
%if 0%{?fedora}
%define anaconda_core_version %{fedora}
%endif

Name:           oscap-anaconda-addon
Version:        1.0
Release:        14%{?dist}
Summary:        Anaconda addon integrating OpenSCAP to the installation process

License:        GPL-2.0-or-later
URL:            https://github.com/OpenSCAP/oscap-anaconda-addon

# This is a Red Hat maintained package which is specific to
# our distribution.
#
# The source is thus available only from within this SRPM
# or via direct git checkout:
# git clone https://github.com/OpenSCAP/oscap-anaconda-addon.git
Source0:        https://github.com/OpenSCAP/oscap-anaconda-addon/releases/download/r%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  python3-pycurl
BuildRequires:  openscap openscap-utils openscap-python3
BuildRequires:  anaconda-core >= %{anaconda_core_version}
Requires:       anaconda-core >= %{anaconda_core_version}
Requires:       python3-cpio
Requires:       python3-pycurl
Requires:       python3-kickstart
Requires:       openscap openscap-utils openscap-python3
Requires:       scap-security-guide

%description
This is an addon that integrates OpenSCAP utilities with the Anaconda installer
and allows installation of systems following restrictions given by a SCAP
content.

%prep
%autosetup -n %{name}-%{version}


%build

#%check

%install
make install DESTDIR=%{buildroot}
%find_lang %{name}

%files -f %{name}.lang
%{_datadir}/anaconda/addons/org_fedora_oscap

%doc COPYING ChangeLog README.md

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 08 2021 Matej Tyc <matyc@redhat.com> - 1.0-9
- Modified the spec file to be compatible with the RHEL one.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Matěj Týč <matyc@redhat.com> - 1.0-5
- Disabled execution of tests, as they are not meant to be executed in the build environment.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Matěj Týč <matyc@redhat.com> - 1.0-1
- Rebased to upstream version 1.0
- Python3 support, anaconda 28 support.

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7-7
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 07 2015 Vratislav Podzimek <vpodzime@redhat.com> - 0.7-1
- Adapt to changes in Anaconda
- Define name of the spoke window
- Set fetching flag to False when extraction error happens
- Remove code that was pushed to the anaconda's sources

* Fri Feb 28 2014 Vratislav Podzimek <vpodzime@redhat.com> - 0.6-2
- Rebuild with building issues fixed

* Fri Feb 28 2014 Vratislav Podzimek <vpodzime@redhat.com> - 0.6-1
- Getting status needs to run in the main thread
- Grab focus for the URL entry after switching notebook page
- Clear rule data when unselecting profile
- Update message as part of the initialization
- Add BuildRequires: gettext
- Include translations in the tarball and RPM

* Fri Feb 28 2014 Vratislav Podzimek <vpodzime@redhat.com> - 0.5-1
- Allow users to change content
- Show and hide control buttons properly
- Fix sensitivity of the URL entry and fetch button
- Add the button allowing users to use SSG content if available
- Fix listing python sources when creating potfile and regenerate it
- Omit the %%addon section from kickstart in dry-run mode
- Implement the dry-run mode in the GUI (trac#2)
- Add UI elements for content changing and dry-run mode
- Check content_defined instead of content_url in the GUI code
- First select the profile, then update the message store
- Remove unused import
- Ignore some more temporary/backup files
- If no content is specified and SSG is available, use it
- New special content type -- SCAP Security Guide
- Fix name of the property used when doing fingerprint check
- Get rid of an unused variable
- Fix data fetch locking to work properly with kickstart installations
- Use 'anonymous:' if no username and password is given for FTP
- Initial version of the translations template file
- First steps to dry-run mode
- Fix main notebook tabs
- Make translations work
- Manipulation with the i18n related files
- If no profile is given, default to default
- Ignore updates.img and its auxiliary directory
- Catch only fetching errors from the fetching thread
- Do not allow multiple simultaneous fetches/initializations
- Prevent user from changing the URL while we try to fetch from it
- Add support for the Default profile
- Support FTP as a content source (#1050980)
- React properly on archive extraction failure
- Refactor the code pre-processing the fetched content
- Unify exceptions from archive extraction
- Make pylint check mandatory to pass
- Support for hash based content integrity checking

* Tue Jan 14 2014 Vratislav Podzimek <vpodzime@redhat.com> - 0.4-1
- Beware of running Gtk actions from a non-main thread
- Fix path to the tailoring file when getting rules
- A git hook for running tests when pushing
- Inform user if no profile is selected
- Visually mark the selected profile
- Better UX with content URL entry and progress label
- React on invalid content properly (#1032846)
- Stop spinner when data fetching is finished
- Make the data fetching thread non-fatal (#1049989)
- Exit code 2 from the oscap tool is not an error for us (#1050913)
- Be ready to work with archives/RPMs containing data streams
- Add unit tests for the keep_type_map function
- Add support for namedtuples to keep_type_map
- Add target for running pylint check
- Add target for running just unittests
- On the way to tailoring
- Tests for kickstart XCCDF tailoring handling
- Kickstart support for XCCDF tailoring
- Check session validity also when using XCCDF benchmark

* Tue Dec 10 2013 Vratislav Podzimek <vpodzime@redhat.com> - 0.3-1
- Implement and use our own better function for joining paths
- The content entry should have focus if there is no content
- RPM is just a weird archive in the pre-installation phase
- Ignore RPM files as well
- Adapt tests to dir constants now ending with "/"
- CpioArchive cannot be created from a piped output
- Fix namespace definitions in the testing XCCDF file
- Prevent putting None into xccdf_session_is_sds
- Fix the __all__ variable in the common module
- Strip content dir prefix when setting xccdf/cpe paths
- Inform user we now support archive URLs as well
- Ignore various file types in the git repository
- Try to find content files in the fetched archive or RPM
- Run pylint -E as part of the test target
- Return list of extracted files/directories when extracting archive
- Do not try to search for empty file paths in archives
- Properly set the content type based on the URL's suffix
- Switch profiles on double-click
- Hook urlEntry's activate signal to fetchButton click
- Save the spoke's glade file with a new Glade
- The addon now requires the python-cpio package
- Use really_hide for the UI elements for datastream-id and xccdf-id
- Support for RPM content in the GUI spoke
- RPM content support for kickstart processing
- Add property for the raw post-installation content path
- Make content type case insensitive
- Rest of the code needed for RPM extraction
- Actually look for the file path in entry names
- Basic stuff needed for the RPM content support
- Run tests in paralel
- Specify files in a better way in spec

* Mon Oct 21 2013 Vratislav Podzimek <vpodzime@redhat.com> - 0.2-1
- Initial RPM for the oscap-anaconda-addon
