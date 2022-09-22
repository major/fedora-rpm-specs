%global forgeurl https://github.com/debrouxl/tilibs
%global commit 8ffa244e522a484146fe0d7c1130a554f8dba48e
%if 0%{?el7}
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global forgesource %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
%global date 20220228
%else
%forgemeta
%endif

# tilibs needs to install some of the libraries during the build to link
# against them, so we define a temporary destdir to avoid polluting the
# buildroot and add it to the build flags
%global build_destdir %{_builddir}/build_destdir
%global optflags %{optflags} -I%{build_destdir}%{_includedir}/tilp2 -L%{build_destdir}%{_libdir}

Name:           tilibs
# Each library has its own version number, but the overall project is versioned
# together with tilp
Version:        1.19
%if 0%{?el7}
Release:        %autorelease -s %{date}git%{shortcommit}
%else
Release:        %autorelease
%endif
Summary:        Texas Instruments calculators interface libraries

License:        GPLv2+
URL:            http://lpg.ticalc.org/prj_tilp
Source0:        %{forgesource}
# The udev rule is needed when using systemd < 251
# https://github.com/systemd/systemd/pull/22307
Source1:        69-libticables.rules

%if 0%{?el7}
BuildRequires:  cmake3
%else
BuildRequires:  cmake
%endif
BuildRequires:  gcc-c++
BuildRequires:  sed
%if 0%{?el7}
BuildRequires:  systemd
%else
BuildRequires:  systemd-rpm-macros
%endif
BuildRequires:  tfdocgen

BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  libarchive-devel
%if 0%{?fedora}
BuildRequires:  libusb1-devel
%elif 0%{?el7}
BuildRequires:  libusbx-devel
%else
BuildRequires:  libusb-devel
%endif
BuildRequires:  zlib-devel

%description
Set of libraries to interface with Texas Instruments calculators.

%package        devel
Summary:        Development files for tilibs
Requires:       libticables%{?_isa} = %{version}-%{release}
Requires:       libticalcs%{?_isa} = %{version}-%{release}
Requires:       libticonv%{?_isa} = %{version}-%{release}
Requires:       libtifiles%{?_isa} = %{version}-%{release}
Requires:       glib2-devel
Requires:       libarchive-devel
%if 0%{?fedora}
Requires:       libusb1-devel
%elif 0%{?el7}
Requires:       libusbx-devel
%else
Requires:       libusb-devel
%endif
Requires:       zlib-devel
Provides:       libticables-devel = %{version}-%{release}
Provides:       libticalcs-devel = %{version}-%{release}
Provides:       libticonv-devel = %{version}-%{release}
Provides:       libtifiles-devel = %{version}-%{release}
# Replace retired packages in F35, remove once F37 is branched
Obsoletes:      libticables2-devel < 1.3.5-13
Provides:       libticables2-devel = %{version}-%{release}
Obsoletes:      libticalcs2-devel < 1.1.9-13
Provides:       libticalcs2-devel = %{version}-%{release}
Obsoletes:      libtifiles2-devel < 1.1.7-14
Provides:       libtifiles2-devel = %{version}-%{release}

%description    devel
Include files and libraries for linking and developing applications using
libticables, libticalcs, libticonv and libtifiles.

%package -n     libticables
Summary:        Texas Instruments link cables library
%if 0%{?el7}
Requires:       udev
%else
Requires:       systemd-udev
%endif
# Replace retired packages in F35, remove once F37 is branched
Obsoletes:      libticables2 < 1.3.5-13
Provides:       libticables2 = %{version}-%{release}

%description -n libticables
The ticables library is able to handle the different link cables designed for
Texas Instruments's graphing calculators (also called handhelds) in a fairly
transparent fashion. With this library, the developer does not have to worry
about the different link cables' characteristics as well as the different
platforms. The library provides a complete API which is very easy to use and
makes things easier.

%package -n     libticables-doc
Summary:        HTML documentation for libticables
BuildArch:      noarch
# Replace retired packages in F35, remove once F37 is branched
Obsoletes:      libticables2-doc < 1.3.5-13
Provides:       libticables2-doc = %{version}-%{release}

%description -n  libticables-doc
HTML documentation for linking and developing applications using libticables.

%package -n     libticalcs
Summary:        Texas Instruments calculator communication library
# Replace retired packages in F35, remove once F37 is branched
Obsoletes:      libticalcs2 < 1.1.9-13
Provides:       libticalcs2 = %{version}-%{release}

%description -n libticalcs
The ticalcs library is a library which brings about all the functions needed to
communicate with a Texas Instruments graphing calculator (or hand-held).
Currently, it does not support some education devices (such as CBL/CBR and
others). This library is able to communicate with handhelds in a fairly
transparent fashion. With this library, the developer does not have to worry
about the packet oriented protocol, the file management and some other stuff.

%package -n     libticalcs-doc
Summary:        HTML documentation for libticalcs
BuildArch:      noarch
# Replace retired packages in F35, remove once F37 is branched
Obsoletes:      libticalcs2-doc < 1.1.9-13
Provides:       libticalcs2-doc = %{version}-%{release}

%description -n  libticalcs-doc
HTML documentation for linking and developing applications using libticalcs.

%package -n     libticonv
Summary:        Texas Instruments calculators charsets library

%description -n libticonv
The ticonv library is a library capable of conversions between Texas
Instruments character sets and UTF-8/UTF-16 character sets.

%package -n     libticonv-doc
Summary:        HTML documentation for libticables
BuildArch:      noarch

%description -n  libticonv-doc
HTML documentation for linking and developing applications using libticonv.

%package -n     libtifiles
Summary:        Texas Instruments calculator communication library
# Replace retired packages in F35, remove once F37 is branched
Obsoletes:      libtifiles2 < 1.1.7-14
Provides:       libtifiles2 = %{version}-%{release}

%description -n libtifiles
The tifiles library is a library capable of reading, modifying, and writing TI
formatted files. It can also group/ungroup files. This library is able to
manipulate files in a fairly transparent fashion. With this library, the
developer does not have to worry about the different file formats.

%package -n     libtifiles-doc
Summary:        HTML documentation for libtifiles
BuildArch:      noarch
# Replace retired packages in F35, remove once F37 is branched
Obsoletes:      libtifiles2-doc < 1.1.7-14
Provides:       libtifiles2-doc = %{version}-%{release}

%description -n  libtifiles-doc
HTML documentation for linking and developing applications using libtifiles.

%prep
%if 0%{?el7}
%autosetup -n %{name}-%{commit} -p1

# Drop unsupported flag
sed -i 's/-Werror=date-time//' CMakeLists.txt
%else
%forgeautosetup -p1
%endif

# Fix line endings
sed -i 's/\r$//' lib*/trunk/LOGO lib*/trunk/docs/html/style.css
rm lib*/trunk/docs/html/clean.bat

# Convert to UTF-8
for dir in lib*; do
  iconv -f iso8859-1 -t utf-8 ${dir}/trunk/LOGO > LOGO.conv && mv -f LOGO.conv ${dir}/trunk/LOGO
done

%build
export DESTDIR="%{build_destdir}"
%if 0%{?el7}
%cmake3
%cmake3_build
%else
%cmake
%cmake_build
%endif

# Build docs
for dir in lib*; do
  pushd ${dir}/trunk/docs && tfdocgen ../ && popd
done

%check
# The tests use a non-standard target, so we have to run the manually
export DESTDIR="%{build_destdir}"
%if 0%{?el7}
%cmake3_build --target check
%else
%cmake_build --target check
%endif

%install
%if 0%{?el7}
%cmake3_install
%else
%cmake_install
%endif
%find_lang libticables2
%find_lang libticalcs2
%find_lang libtifiles2

# Install the udev rule
%if 0%{?el7}
mkdir -p %{buildroot}%{_udevrulesdir}
%endif
install -Dpm0644 -t %{buildroot}%{_udevrulesdir} %SOURCE1

# We don't want static libraries
rm %{buildroot}%{_libdir}/*.a

%files devel
# The license is the same for all libraries so just pick one here
%license libticables/trunk/COPYING
%{_includedir}/tilp2
%{_libdir}/libti*.so
%{_libdir}/pkgconfig/ti*.pc

%files -n libticables -f libticables2.lang
%license libticables/trunk/COPYING
%doc libticables/trunk/AUTHORS libticables/trunk/ChangeLog libticables/trunk/LOGO libticables/trunk/README
%{_libdir}/libticables2.so.*
%{_udevrulesdir}/69-libticables.rules

%files -n libticables-doc
%license libticables/trunk/COPYING
%doc libticables/trunk/docs/html

%files -n libticalcs -f libticalcs2.lang
%license libticalcs/trunk/COPYING
%doc libticalcs/trunk/AUTHORS libticalcs/trunk/ChangeLog libticalcs/trunk/LOGO libticalcs/trunk/README
%{_libdir}/libticalcs2.so.*

%files -n libticalcs-doc
%license libticalcs/trunk/COPYING
%doc libticalcs/trunk/docs/html

%files -n libticonv
%license libticonv/trunk/COPYING
%doc libticonv/trunk/AUTHORS libticonv/trunk/ChangeLog libticonv/trunk/LOGO libticonv/trunk/README
%{_libdir}/libticonv.so.*

%files -n libticonv-doc
%license libticonv/trunk/COPYING
%doc libticonv/trunk/docs/html

%files -n libtifiles -f libtifiles2.lang
%license libtifiles/trunk/COPYING
%doc libtifiles/trunk/AUTHORS libtifiles/trunk/ChangeLog libtifiles/trunk/LOGO libtifiles/trunk/README
%{_libdir}/libtifiles2.so.*

%files -n libtifiles-doc
%license libtifiles/trunk/COPYING
%doc libtifiles/trunk/docs/html

%changelog
%autochangelog
