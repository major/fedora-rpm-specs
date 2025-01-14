%global repo_name vcpkg-tool
%global repo_tag 2025-01-11

Name: vcpkg
Version: %(echo %{repo_tag} | sed 's/-/./g')
Release: %autorelease

License: MIT
Summary: C++ Library Manager
URL: https://github.com/microsoft/%{repo_name}
Source0: %{url}/archive/%{repo_tag}/%{name}-%{version}.tar.gz
Source1: %{name}.sh

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} && 0%{?fedora} >= 42
ExcludeArch: %{ix86}
%endif

BuildRequires: catch-devel >= 2.13.0
BuildRequires: cmake
BuildRequires: cmrc-devel
BuildRequires: fmt-devel >= 11.0.0
BuildRequires: gcc-c++
BuildRequires: ninja-build

Requires: cmake%{?_isa}
Requires: curl%{?_isa}
Requires: gcc-c++%{?_isa}
Requires: git-core%{?_isa}
Requires: ninja-build%{?_isa}

Recommends: aria2%{?_isa}

%description
Vcpkg is a package manager for the different C and C++ libraries.

Vcpkg can collect usage data. The data collected by Microsoft is anonymous.

This package has telemetry disabled by default and doesn't ship the
repository with recipes.

Please read README.fedora file for more information.

%prep
%autosetup -n %{repo_name}-%{repo_tag} -p1

# Adding a file with some useful information...
cat << EOF >> README.fedora
Fedora package has telemetry disabled by default. If you want to enable
it, you should unset the VCPKG_DISABLE_METRICS environment variable
from the %{_sysconfdir}/profile.d/%{name}.sh file.

Fedora can't ship the official Git repository with recipes for various
reasons (especially legal), so you'll need to manually clone it into
the \$HOME/.local/share/%{name} directory (the path can be changed in
the %{_sysconfdir}/profile.d/%{name}.sh file):
git clone https://github.com/microsoft/%{name} \$VCPKG_ROOT

You will have to update it manually too:
git -C \$VCPKG_ROOT pull
EOF

# Fixing line endings...
sed -e "s,\r,," -i README.md

# Unbundling catch...
rm -rf include/catch2
ln -svf %{_includedir}/catch2/ include/

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
    -DBUILD_TESTING:BOOL=OFF \
    -DVCPKG_BASE_VERSION:STRING="%{repo_tag}" \
    -DVCPKG_VERSION:STRING="%{release}" \
    -DVCPKG_DEVELOPMENT_WARNINGS:BOOL=OFF \
    -DVCPKG_WARNINGS_AS_ERRORS:BOOL=OFF \
    -DVCPKG_DEPENDENCY_CMAKERC:BOOL=ON \
    -DVCPKG_DEPENDENCY_EXTERNAL_FMT:BOOL=ON \
    -DVCPKG_BUILD_TLS12_DOWNLOADER:BOOL=OFF \
    -DVCPKG_BUILD_FUZZING:BOOL=OFF \
    -DVCPKG_EMBED_GIT_SHA:BOOL=OFF \
    -DVCPKG_BUILD_BENCHMARKING:BOOL=OFF \
    -DVCPKG_ADD_SOURCELINK:BOOL=OFF
%cmake_build

%install
%cmake_install

# Installing environment options override...
install -D -m 0644 -p "%{SOURCE1}" "%{buildroot}%{_sysconfdir}/profile.d/%{name}.sh"

%files
%doc README.md README.fedora
%license LICENSE.txt NOTICE.txt
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.sh

%changelog
%autochangelog
