%{!?tcl_sitearch: %define tcl_sitearch %{_libdir}/tcl%(echo 'puts $tcl_version' | tclsh)}

Name:           tdom
Version:        0.9.6
Release:        %autorelease
Summary:        DOM parser for Tcl

# tdom itself is MPL-2.0, bundled expat code is MIT.
#
# tdom can be built against system-provided expat, but even then,
# it embeds some value tables that expat does not expose in include headers.
License:        MPL-2.0 AND MIT
URL:            http://www.tdom.org
Source0:        http://tdom.org/downloads/%{name}-%{version}-src.tgz

BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tcl-devel
Requires:       tcl(abi) >= 8.5

%description
tDOM combines high performance XML data processing with easy and powerful Tcl
scripting functionality. tDOM should be one of the fastest ways to manipulate
XML with a scripting language and uses very little memory.

%package devel
Summary: Development files for compiling against tdom
Requires:       %{name} = %{version}-%{release} expat-devel
%description devel
Development header files for compiling against tdom.

%prep
%autosetup -p1 -n %{name}-%{version}-src

%build
%configure --enable-threads --with-expat=yes
%make_build

%install
%make_install

mkdir -p %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/%{name}%{version}/*.so %{buildroot}%{_libdir}
mv %{buildroot}%{_libdir}/%{name}%{version}/*.a %{buildroot}%{_libdir}
mv %{buildroot}%{_libdir}/%{name}%{version} %{buildroot}%{tcl_sitearch}

# Adjust some paths to reflect the new file locations
sed -i -e 's/file join $dir libtdom/file join $dir .. .. libtdom/' %{buildroot}%{tcl_sitearch}/%{name}%{version}/pkgIndex.tcl

sed -i -e "s#%{_libdir}/%{name}%{version}#%{_libdir}#" %{buildroot}%{_libdir}/tdomConfig.sh

%files
%doc README.md CHANGES ChangeLog doc/*.html
%license MPL_2.0.html expat/COPYING
%{tcl_sitearch}/%{name}%{version}
%{_libdir}/*.so
%exclude %{_libdir}/*.a
%{_mandir}/mann/*.gz

%files devel
%{_libdir}/%{name}Config.sh
# This static library is a 'stub' library that is used to assist with
# shared lib linking across library versions:  http://wiki.tcl.tk/285
%{_libdir}/*.a
%{_includedir}/*.h


%changelog
%autochangelog
