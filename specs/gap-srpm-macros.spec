Name:           gap-srpm-macros
Version:        2
Release:        %autorelease
Summary:        Macros for building GAP source RPMs

License:        MIT
URL:            https://src.fedoraproject.org/rpms/gap-srpm-macros
BuildArch:      noarch
Source0:        macros.gap-srpm
Source1:        LICENSE

%description
This package contains macros needed by RPM in order to build source RPMS for
GAP packages.

%prep
%setup -q -T -c
install -pm 0644 %{SOURCE1} .

%install
mkdir -p %{buildroot}%{rpmmacrodir}
install -pm 0644 %{SOURCE0} %{buildroot}%{rpmmacrodir}/macros.gap-srpm

%files
%license LICENSE
%{rpmmacrodir}/macros.gap-srpm

%changelog
%autochangelog
