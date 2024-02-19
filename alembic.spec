# Force out of source build
%undefine __cmake_in_source_build
#%%global prerelease _beta2
# TODO:
# Python Module

Name:           alembic
Version:        1.8.6
Release:        %autorelease
Summary:        Open framework for storing and sharing scene data
License:        BSD-3-Clause AND BSL-1.0
URL:            http://alembic.io/

Source0:        https://github.com/%{name}/%{name}/archive/%{version}%{?prerelease}.tar.gz#/%{name}-%{version}%{?prerelease}.tar.gz

# Use patch from Gentoo fixing iblmbase root path
# https://gitweb.gentoo.org/repo/gentoo.git/tree/media-gfx/alembic/files/alembic-1.7.11-0002-Find-IlmBase-by-setting-a-proper-ILMBASE_ROOT-value.patch?id=953b3b21db55df987dd8006dcdec19e945294d98
Patch0:         alembic-1.7.11-0002-Find-IlmBase-by-setting-a-proper-ILMBASE_ROOT-value.patch 
BuildRequires:  boost-devel
BuildRequires:  cmake >= 3.13
BuildRequires:	gcc-c++
BuildRequires:  hdf5-devel

# Per https://github.com/alembic/alembic/blob/master/README.txt
# alembic actually needs ilmbase, not OpenEXR.
# As of OpenEXR 3.x Imath is now a standalone library.
%if 0%{?fedora} > 34
BuildRequires:  cmake(Imath)
%else
BuildRequires:  pkgconfig(IlmBase)
%endif
BuildRequires:  pkgconfig(zlib)

%description
Alembic is an open computer graphics interchange framework. Alembic distills
complex, animated scenes into a non-procedural, application-independent set of
baked geometric results. This 'distillation' of scenes into baked geometry is
exactly analogous to the distillation of lighting and rendering scenes into
rendered image data.

%package        libs
Summary:        Core Alembic libraries

%description    libs
Alembic is an open computer graphics interchange framework. Alembic distills
complex, animated scenes into a non-procedural, application-independent set of
baked geometric results. This 'distillation' of scenes into baked geometry is
exactly analogous to the distillation of lighting and rendering scenes into
rendered image data.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}%{?prerelease}

sed -i -e 's/ConfigPackageLocation lib/ConfigPackageLocation %{_lib}/g' \
    lib/Alembic/CMakeLists.txt

iconv -f iso8859-1 -t utf-8 ACKNOWLEDGEMENTS.txt > ACKNOWLEDGEMENTS.txt.conv && \
    mv -f ACKNOWLEDGEMENTS.txt.conv ACKNOWLEDGEMENTS.txt

%build
export CXXFLAGS="%{optflags} -Wl,--as-needed"
%cmake %{?_cmake_skip_rpath} \
    -DALEMBIC_LIB_INSTALL_DIR=%{_libdir} \
    -DALEMBIC_SHARED_LIBS=ON \
    -DCMAKE_CXX_STANDARD=17 \
    -DUSE_BINARIES=ON \
    -DUSE_HDF5=ON \
    -DUSE_EXAMPLES=ON \
    -DUSE_PYALEMBIC=OFF \
    -DUSE_STATIC_BOOST=OFF \
    -DUSE_STATIC_HDF5=OFF \
    -DUSE_TESTS=ON

%cmake_build

%install
%cmake_install

%files
%{_bindir}/abcconvert
%{_bindir}/abcdiff
%{_bindir}/abcecho
%{_bindir}/abcechobounds
%{_bindir}/abcls
%{_bindir}/abcstitcher
%{_bindir}/abctree

%files libs
%license LICENSE.txt
%doc ACKNOWLEDGEMENTS.txt FEEDBACK.txt NEWS.txt README.txt
%{_libdir}/libAlembic.so.*

%files devel
%{_includedir}/Alembic
%{_libdir}/cmake/Alembic
%{_libdir}/libAlembic.so

%changelog
%autochangelog
