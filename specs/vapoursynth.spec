Name:       vapoursynth
Version:    79
Release:    %autorelease
Summary:    Video processing framework with simplicity in mind
License:    LGPL-2.1-only
URL:        http://www.vapoursynth.com

Source0:    https://github.com/%{name}/%{name}/archive/R%{version}/%{name}-R%{version}.tar.gz
# Restore soversion that was dropped when libvapoursynth-script was renamed to libvsscript.
Patch0:     %{name}-vsscript-soversion.patch
# Check for _Float16 instead of assuming that everything not x86 provides it.
Patch1:     %{name}-float16-native-check.patch

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(zimg)
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

# Since R79 upstream installs the whole runtime -- the core library, the filter
# plugins, vspipe, the headers and the pkg-config file -- inside the Python
# package directory, and VSCore locates libvapoursynthfilters and the
# third-party plugin directory relative to libvapoursynth.so via dladdr().
# The libraries, vspipe and the plugin directory therefore have to stay there;
# see %%install for the FHS entry points layered on top.
%global vsdir %{python3_sitearch}/%{name}

%description
VapourSynth is an application for video manipulation. Or a plugin. Or a library.
It’s hard to tell because it has a core library written in C++ and a Python
module to allow video scripts to be created.

%package        libs
Summary:        VapourSynth's core library with a C++ API
Obsoletes:      lib%{name} < %{version}-%{release}
Provides:       lib%{name} == %{version}-%{release}
Obsoletes:      %{name}-plugins < %{version}-%{release}
Provides:       %{name}-plugins == %{version}-%{release}

%description    libs
VapourSynth's core library with a C++ API.

%package -n     python3-%{name}
Summary:        Python interface for VapourSynth
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
Python interface for VapourSynth/VSSCript.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%package        tools
Summary:        Extra tools for VapourSynth
Requires:       python3-vapoursynth%{?_isa} = %{version}-%{release}

%description    tools
This package contains the vspipe tool for interfacing with VapourSynth.

%prep
%autosetup -p1 -n %{name}-R%{version}

%generate_buildrequires
%pyproject_buildrequires -R

%build
# CPython 3.15 gained a platform specific stable ABI suffix
# (.abi3-x86_64-linux-gnu.so) which meson-python 0.20 does not recognise as
# abi3, so it refuses to build the wheel. Nothing is gained from the limited
# API in a distribution build against a single Python version, so turn it off.
%pyproject_wheel -C setup-args=-Dpython.allow_limited_api=false

%install
%pyproject_install
%pyproject_save_files -l %{name}

# Let RPM pick up docs in the files section.
rm -fr %{buildroot}%{_docdir}/%{name}

# Third-party plugins are auto-loaded from next to the core library.
mkdir -p %{buildroot}%{vsdir}/plugins

# Headers belong in the usual place.
mkdir -p %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{vsdir}/include/*.h %{buildroot}%{_includedir}/%{name}/
rmdir %{buildroot}%{vsdir}/include

# Upstream's vapoursynth.pc resolves everything relative to ${pcfiledir}, which
# no longer works once the file sits in %%{_libdir}/pkgconfig, and it ships no
# Libs: at all. Write it out instead.
rm -fr %{buildroot}%{vsdir}/pkgconfig
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cat > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc <<EOF
prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}/%{name}

Name: vapoursynth
Description: A frameserver for the 21st century
Version: %{version}
Cflags: -I\${includedir}
Libs: -L\${libdir} -lvapoursynth
EOF

# Make the libraries linkable and resolvable the normal way.
mkdir -p %{buildroot}%{_libdir}
for lib in $(cd %{buildroot}%{vsdir} && ls libvapoursynth.so.* libvsscript.so.*); do
    ln -s %{vsdir}/${lib} %{buildroot}%{_libdir}/${lib}
    ln -s ${lib} %{buildroot}%{_libdir}/${lib%%.so.*}.so
done

# The core library, its filter plugins and vspipe live inside the Python
# package directory but are packaged in the -libs and -tools subpackages.
sed -i -e '\#/%{name}/lib.*\.so#d' \
       -e '\#/%{name}/vspipe$#d' \
       -e '\#/%{name}/include#d' \
       -e '\#/%{name}/pkgconfig#d' \
       -e '\#^%%dir %{vsdir}$#d' \
       %{pyproject_files}

%check
%pytest

%files libs
%doc ChangeLog
%license COPYING.LESSER
%dir %{vsdir}
%dir %{vsdir}/plugins
%{vsdir}/lib%{name}.so.*
%{vsdir}/lib%{name}filters*.so
%{vsdir}/libvsscript.so.*
%{_libdir}/lib%{name}.so.*
%{_libdir}/libvsscript.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/libvsscript.so
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%{_bindir}/%{name}
%{_bindir}/vspipe
%{vsdir}/vspipe

%files -n python3-%{name} -f %{pyproject_files}

%changelog
%autochangelog
