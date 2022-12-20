Name:           plotmm
Version:        0.1.2
Release:        %autorelease
Summary:        GTKmm plot widget for scientific applications
License:        LGPLv2
URL:            http://plotmm.sourceforge.net/
Source0:        https://download.sourceforge.net/plotmm/plotmm-%{version}.tar.gz
# Fix code to build against libsigc++20
# Upstream:
# https://sourceforge.net/tracker/?func=detail&atid=632478&aid=2082337&group_id=102665
Patch0:         plotmm-0.1.2-libsigc++20.patch
Patch1:         plotmm-configure-c99.patch
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hardlink
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  pkgconfig(gtkmm-2.4)


%description
This package provides an extension to the gtkmm library. It contains widgets
which are primarily useful for technical and scientifical purposes.

%package devel
Summary:        Headers for developing programs that will use plotmm
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(gtkmm-2.4)
Obsoletes:      %{name}-devel < 0.1.2-35


%description devel
This package contains the headers that programmers will need to develop
applications which will use plotmm.


%package devel-doc
Summary:        Documentation for developing programs that will use plotmm
Requires:       %{name}-devel = %{version}-%{release}
Obsoletes:      %{name}-devel < 0.1.2-35
BuildArch:      noarch


%description devel-doc
This package contains the documentation that programmers will need to develop
applications which will use plotmm.


%package -n plotmm-examples
Summary:    Plotmm sample applications
Requires:   %{name}%{?_isa} = %{version}-%{release}


%description -n plotmm-examples
Plotmm sample applications: plotmm-curves, plotmm-simple


%prep
%setup -q -n plotmm-%{version}
%patch0 -p1 -b .libsigc++20
%patch1 -p1 -b .c99

%build
%configure --disable-rpath --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
mv %{buildroot}%{_bindir}/curves %{buildroot}%{_bindir}/plotmm-curves
mv %{buildroot}%{_bindir}/simple %{buildroot}%{_bindir}/plotmm-simple
install -d %{buildroot}%{_pkgdocdir}-devel-doc
cp -pr doc/html %{buildroot}%{_pkgdocdir}-devel-doc/
hardlink %{buildroot}%{_pkgdocdir}-devel-doc/html


%files
# FSF address is outdated, filed upstream: https://sourceforge.net/p/plotmm/bugs/5/
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/libplotmm.so.0
%{_libdir}/libplotmm.so.0.*

%files devel
%{_includedir}/plotmm/
%{_libdir}/libplotmm.so
%{_libdir}/pkgconfig/*.pc

%files devel-doc
%doc %{_pkgdocdir}-devel-doc/html

%files -n plotmm-examples
%{_bindir}/plotmm-curves
%{_bindir}/plotmm-simple

%changelog
%autochangelog
