Name:           fpc-srpm-macros
Version:        1.3
Release:        %autorelease
Summary:        RPM macros needed by packages built with Free Pascal Compiler
# This package only exist in Fedora repositories
# The license is the standard (MIT) specified in
# Fedora Project Contribution Agreement
# and as URL we provide dist-git URL
License:        MIT
URL:            https://src.fedoraproject.org/rpms/fpc-srpm-macros
Source0:        macros.fpc-srpm
BuildArch:      noarch


%description
This package contains RPM macros needed by packages built with the
Free Pascal Compiler. For example, it makes available a macro that
lists all architectures where fpc is available.

%prep
# nothing to do


%build
# nothing to do


%install
mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d
install -p -m 0644 -t %{buildroot}/%{_rpmconfigdir}/macros.d %{SOURCE0}


%files
%{_rpmconfigdir}/macros.d/*



%changelog
%autochangelog
