Name:           folly-rpm-macros
Version:        37
Release:        %autorelease
Summary:        Common RPM macros for the Folly stack

License:        MIT
URL:            https://src.fedoraproject.org/rpms/folly-rpm-macros
Source0:        macros.folly-rpm
Source1:        macros.folly-srpm

BuildArch:      noarch

Requires:       rpm

%global _description %{expand:

folly-rpm-macros contains common RPM macros for building Folly and other
software that depends on it.

You should not need to install this package manually as folly-devel pulls it in.}

%description %{_description}


%package -n folly-srpm-macros
Summary:        RPM macros for building Folly source packages
Requires:       rpm

%description -n folly-srpm-macros %{_description}

This package contains the macros needed for building Folly source packages.


%prep


%build


%install
install -D -p -m 0644 -t %{buildroot}%{_rpmmacrodir} %{SOURCE0} %{SOURCE1}


%files
%{_rpmmacrodir}/macros.folly-rpm

%files -n folly-srpm-macros
%{_rpmmacrodir}/macros.folly-srpm


%changelog
%autochangelog
