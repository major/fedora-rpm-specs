Name:           atinout
Summary:        AT commands as input are sent to modem and responses given as output
Version:        0.9.1
Release:        6%{?dist}
License:        GPLv3+

URL:            https://atinout.sourceforge.net/
Source0:        https://sourceforge.net/projects/%{name}/files/%{name}-%{version}.tar.gz

# Remove the custom build flags that override fedora build flags, continue to append -DVERSION for build to succeed 
Patch0:        0001-remove-custom-flags.patch

BuildRequires:  gcc
BuildRequires: make

%global _hardened_build 1

%description
This program will read a file (or stdin) containing a list of AT
commands. Each command will be send to the modem, and all the response
for the command will be output to file (or stdout).

%prep
%autosetup

%build
%set_build_flags
%make_build

%install
%make_install

%files
%{_bindir}/atinout
%{_mandir}/man1/atinout.1*
%doc README atinout.1.html logo/atinout.svg
%license gplv3.txt

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 Torrey Sorensen <sorensentor@tuta.io> - 0.9.1-1
- initial packaging
