Name:           flatpak-rpm-macros
Version:        44
Release:        %autorelease
Summary:        Macros for building RPMS for flatpaks
Source0:        macros.flatpak.in
Source1:        distutils.cfg
Source2:        flatpak.xml
Source3:        fontconfig-flatpak.prov
License:        MIT

# Buildrequire these to satisfy Pyton byte-compilation hooks
BuildRequires:  python3-devel

%description
The macros in this package set up the RPM build environment so built
applications install in /app rather than /usr. This package is meant
only for installation in buildroots when rebuilding RPMS to package
in Flatpaks.

%prep

%build
sed -e 's|__LIB__|%{_lib}|g' \
    %{SOURCE0} > macros.flatpak

%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm
install -t $RPM_BUILD_ROOT%{_sysconfdir}/rpm -p -m 644 macros.flatpak
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{python3_version}/distutils/
install -t $RPM_BUILD_ROOT%{_libdir}/python%{python3_version}/distutils/ %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/xdg/xmvn/config.d
install -t $RPM_BUILD_ROOT%{_sysconfdir}/xdg/xmvn/config.d -m 644 %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_rpmconfigdir}
install -t $RPM_BUILD_ROOT%{_rpmconfigdir} -m 755 %{SOURCE3}

%files
# The location in sysconfdir contradicts
# https://fedoraproject.org/wiki/Packaging:Guidelines#Packaging_of_Additional_RPM_Macros
# but I believe is necessary to properly override macros that are otherwise set.
%{_sysconfdir}/rpm/
%{_libdir}/python%{python3_version}/distutils/distutils.cfg
%{_sysconfdir}/xdg/xmvn/config.d/flatpak.xml
%{_rpmconfigdir}/fontconfig-flatpak.prov

%changelog
%autochangelog
