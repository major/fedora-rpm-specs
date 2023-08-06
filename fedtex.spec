Name:           fedtex
Version:        0.2
Release:        %autorelease
Summary:        Simple TeX dependency installer for Fedora

License:        MIT
URL:            https://pagure.io/fedtex
Source0:        https://releases.pagure.org/%{name}/%{name}-%{version}.tar.gz

Requires:       coreutils
Requires:       sed
Requires:       grep

BuildArch:      noarch

%description
%{summary}


%prep
%autosetup


%build
# nothing to build

%install
install -p -m 0755 -D fedtex.sh $RPM_BUILD_ROOT/%{_bindir}/fedtex
install -p -m 0644 -D man/man1/fedtex.1 $RPM_BUILD_ROOT/%{_mandir}/man1/fedtex.1

%files
%license License
%doc Readme.md
%{_mandir}/man1/fedtex.*
%{_bindir}/fedtex



%changelog
%autochangelog
