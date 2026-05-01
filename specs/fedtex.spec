%global forgeurl https://github.com/sanjayankur31/fedtex

Name:           fedtex
Version:        0.2
Release:        %autorelease
Summary:        Simple TeX dependency installer for Fedora

%global tag v%{version}
%forgemeta

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

Requires:       coreutils
Requires:       sed
Requires:       grep

BuildArch:      noarch

%description
%{summary}


%prep
%forgesetup


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
