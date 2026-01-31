%global macros_dir %{_rpmconfigdir}/macros.d

%global macrosfile macros.ghc-srpm

Name:           ghc-srpm-macros
Version:        1.10
Release:        %autorelease
Summary:        RPM macros for building Haskell source packages

License:        GPL-2.0-or-later
URL:            https://src.fedoraproject.org/rpms/ghc-srpm-macros
BuildArch:      noarch

Source0:        %{macrosfile}

%description
Macros used when generating Haskell source RPM packages.


%prep
%{nil}


%build
echo no build stage needed


%install
install -p -D -m 0644 %{SOURCE0} %{buildroot}/%{macros_dir}/%{macrosfile}


%files
%{macros_dir}/%{macrosfile}


%changelog
%autochangelog
