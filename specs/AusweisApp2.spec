# Add generation of HMAC checksums of the final stripped binaries.
# %%define with lazy expansion is used here intentionally, because
# this needs to be expanded inside of a higher level macro that
# gets expanded itself.
%define __spec_install_post                      \
%{?__debug_package:%{__debug_install_post}}      \
%{__arch_install_post}                           \
%{__os_install_post}                             \
fipshmac %{buildroot}%{_bindir}/%{newname}          \\\
  %{buildroot}%{_libexecdir}/%{newname}             \\\
  %{buildroot}%{_datadir}/%{newname}/openssl.cnf    \
c="%{buildroot}%{_datadir}/%{newname}/config.json"  \
if [[ -f ${c} ]]; then                           \
  fipshmac ${c}                                  \
fi                                               \
%{nil}

# Always do out-of-source builds with CMake.
%{?__cmake_in_source_build:%undefine __cmake_in_source_build}

# Do not build non-lto objects to reduce build time significantly.
%global build_cflags   %(echo '%{build_cflags}'   | sed -e 's!-ffat-lto-objects!-fno-fat-lto-objects!g')
%global build_cxxflags %(echo '%{build_cxxflags}' | sed -e 's!-ffat-lto-objects!-fno-fat-lto-objects!g')
%global build_fflags   %(echo '%{build_fflags}' | sed -e 's!-ffat-lto-objects!-fno-fat-lto-objects!g')
%global build_fcflags  %(echo '%{build_fflags}' | sed -e 's!-ffat-lto-objects!-fno-fat-lto-objects!g')

# Build and package Doxygen documentation?
%bcond_without    doxy

# Do we build with Qt6?
%if 0%{?fedora} || 0%{?rhel} >= 9
%global qt6_build 1
%else
%global qt6_build 0
%endif

# Package summary.  Gets overwritten by subpackages otherwise.
%global pkg_sum   Online identification with German ID card (Personalausweis)

# Upstream renamed to AusweisApp with 2.0 release
%global newname   AusweisApp

Name:             AusweisApp2
Version:          2.3.1
Release:          %autorelease
Summary:          %{pkg_sum}

License:          EUPL-1.2
URL:              https://www.ausweisapp.bund.de/en

# Url to releases on github.
%global rel_url   https://github.com/Governikus/%{name}/releases/download/%{version}

# Generate gpg-keyring:
# gpg2 --keyserver keyserver.ubuntu.com --recv-keys 699BF3055B0A49224EFDE7C72D7479A531451088
# gpg2 --export --export-options export-minimal 699BF3055B0A49224EFDE7C72D7479A531451088 > %%{name}-pubring.gpg

Source0000:       %{rel_url}/%{newname}-%{version}.tar.gz
Source0001:       %{rel_url}/%{newname}-%{version}.tar.gz.asc
Source0002:       %{name}-pubring.gpg
Source0003:       %{rel_url}/%{newname}-%{version}.tar.gz.sha256
Source0004:       https://joinup.ec.europa.eu/sites/default/files/custom-page/attachment/2020-03/EUPL-1.2%%20EN.txt#/EUPL-12_EN.txt
Source1000:       gen_openssl_cnf.py

# Downstream.
Patch01000:       %{name}-1.24.1-use_Qt_TranslationsPath.patch
# Needed because Fedora's openssl does not support elliptic curves using custom parameters.
# Request to enable them was denied: https://bugzilla.redhat.com/show_bug.cgi?id=2259403
# It is currently not clear if the legacy API works by accident or by design. It does work as of March 2025.
Patch01001:       %{name}-2.0.1-use-legacy-openssl-api.patch

BuildRequires:    cmake
BuildRequires:    crypto-policies
BuildRequires:    desktop-file-utils
BuildRequires:    gcc-c++
BuildRequires:    gnupg2
BuildRequires:    http-parser-devel
BuildRequires:    libappstream-glib
BuildRequires:    libudev-devel
BuildRequires:    libxkbcommon-devel
BuildRequires:    ninja-build
BuildRequires:    openssl-devel
BuildRequires:    pcsc-lite-devel
BuildRequires:    python3-devel
%if 0%{?qt6_build}
BuildRequires:    qt6-qtbase-devel
BuildRequires:    qt6-qtbase-private-devel
BuildRequires:    qt6-qtscxml-devel
BuildRequires:    qt6-qtshadertools-devel
BuildRequires:    qt6-qtsvg-devel
BuildRequires:    qt6-qttools-devel
BuildRequires:    qt6-qtwebsockets-devel
%else
BuildRequires:    qt5-linguist
BuildRequires:    qt5-qtbase-devel
BuildRequires:    qt5-qtconnectivity-devel
BuildRequires:    qt5-qtdeclarative-devel
BuildRequires:    qt5-qtquickcontrols2-devel
BuildRequires:    qt5-qtsvg-devel
BuildRequires:    qt5-qtwebsockets-devel
%endif
BuildRequires:    %{_bindir}/sha256sum
BuildRequires:    %{_bindir}/fipshmac

# Lowercase package name.
%global lc_name   %{lua:print(string.lower(rpm.expand("%{name}")))}

# Make sure this package automatically replaces the security hazard
# built in some COPR.
Obsoletes:        %{name}                < 1.20.1
Obsoletes:        %{lc_name}             < 1.20.1

# Provide the lowercase name for convenience as well.
Provides:         %{lc_name}             = %{version}-%{release}
Provides:         %{lc_name}%{?_isa}     = %{version}-%{release}

# Do not raise conflicts about shared license files.
Requires:         %{name}-data           = %{version}-%{release}
Requires:         (%{name}-doc           = %{version}-%{release} if %{name}-doc)

%if !0%{?qt6_build}
# RHBZ#1885310
# Needed for the GUI to show up on startup.
Requires:         qt5-qtquickcontrols2%{?_isa}
%endif

# Brainpool ECC
Requires:         openssl-libs%{?_isa}  >= 3.0.8-2

# Needed for running fipscheck on application startup.
# Requires:         fipscheck

%if 0%{?qt6_build}
# Needed for GUI elements to be rendered
Requires:         qt6-qtimageformats%{?_isa}
Requires:         qt6-qtsvg%{?_isa}
%endif

%description
The AusweisApp2 is a software to identify yourself online
with your ID card (Personalausweis) or your electronic
residence permit (Aufenthalts- / Niederlassungserlaubis).

The AusweisApp2 also offers you an integrated self-assessment
in which you are able to view your data that is stored on the
online ID.


%package data
Summary:          Architecture-independent files used by %{name}
BuildArch:        noarch

Requires:         %{name}                = %{version}-%{release}
Requires:         hicolor-icon-theme

%description data
This package contains the architecture-independent files
used by %{name}.


%package doc
Summary:          User and API documentation for %{name}
BuildArch:        noarch

%if %{with doxy}
BuildRequires:    doxygen
BuildRequires:    graphviz
%endif
BuildRequires:    hardlink
BuildRequires:    python3-sphinx
BuildRequires:    python3-sphinx_rtd_theme

# Do not raise conflicts about shared license files.
Requires:         (%{name}               = %{version}-%{release} if %{name})

# The doc-api package is faded, since we can ship the
# Doxygen documentation noarch'ed as well now.
Obsoletes:        %{name}-doc-api        < 1.20.1-2
Provides:         %{name}-doc-api        = %{version}-%{release}

%description doc
This package contains the user and API documentation for %{name}.


%prep
# Verify tarball integrity.
%{gpgverify}                \
  --keyring='%{SOURCE2}'    \
  --signature='%{SOURCE1}'  \
  --data='%{SOURCE0}'
pushd %{_sourcedir}
sha256sum -c %{SOURCE3}
popd

%autosetup -p 1 -n %{newname}-%{version}
install -pm 0644 %{SOURCE4} LICENSE.en.txt

# Generate application specific OpenSSL configuration.
# See the comments in the resulting file for further information.
%{__python3} %{SOURCE1000} resources/config.json.in \
  > fedora_%{name}_openssl.cnf

# Create the shell wrapper.
cat << EOF > fedora_%{name}_wrapper.sh
#!/bin/sh
# /usr/bin/fipscheck                               \\
#     %{_bindir}/%{newname}                         \\
#     %{_libexecdir}/%{newname}                     \\
#     %{_datadir}/%{newname}/config.json           \\
#     %{_datadir}/%{newname}/openssl.cnf           \\
# || exit \$?;
OPENSSL_CONF=%{_datadir}/%{newname}/openssl.cnf  \\
%{_libexecdir}/%{newname} "\$@";
EOF


%build
# The project does not ship any libraries that are meant to be
# consumed externally.  Thus we disable shared libs explicitly.
# See:  https://github.com/Governikus/AusweisApp2/pull/24
# and:  https://github.com/Governikus/AusweisApp2/pull/26
%cmake                                     \
  -DBUILD_SHARED_LIBS:BOOL=OFF             \
  -DBUILD_TESTING:BOOL=OFF                 \
  -DCMAKE_BUILD_TYPE:STRING=Release        \
  -DINTEGRATED_SDK:BOOL=OFF                \
  -DPYTHON_EXECUTABLE:STRING=%{__python3}  \
  -DSELFPACKER:BOOL=OFF                    \
  -DUSE_SMARTEID:BOOL=ON                   \
  -G Ninja
%cmake_build

%if (0%{?fedora} || 0%{?rhel} > 8)
# Documentation.
%cmake_build --target installation_integration notes sdk
%if %{with doxy}
%cmake_build --target doxy
%endif
%else
# Documentation.
%ninja_build -C %{_vpath_builddir} installation_integration notes sdk
%if %{with doxy}
%ninja_build -C %{_vpath_builddir} doxy
%endif
%endif


%install
%cmake_install

# Relocate the application binary so we can call it through
# a shell wrapper and move installed files to proper locations.
mkdir -p %{buildroot}{%{_libexecdir},%{_qt5_translationdir}}
mv %{buildroot}%{_bindir}/%{newname} %{buildroot}%{_libexecdir}/%{newname}

# Install the shell wrapper and custom OpenSSL configuration.
install -pm 0755 fedora_%{name}_wrapper.sh %{buildroot}%{_bindir}/%{newname}
install -pm 0644 fedora_%{name}_openssl.cnf   \
  %{buildroot}%{_datadir}/%{newname}/openssl.cnf

# Move translation in proper location.
%if !(0%{?qt6_build})
mv %{buildroot}%{_datadir}/%{newname}/translations/* \
  %{buildroot}%{_qt5_translationdir}
rm -fr %{buildroot}%{_datadir}/%{newname}/translations
%endif

# Excessive docs.
mkdir -p %{buildroot}%{_pkgdocdir}/{installation_integration,notes,sdk}
install -pm 0644 README.rst %{buildroot}%{_pkgdocdir}
%if %{with doxy}
mkdir -p %{buildroot}%{_pkgdocdir}/doxy
cp -a %{_vpath_builddir}/doc/html/* %{buildroot}%{_pkgdocdir}/doxy
%endif
cp -a %{_vpath_builddir}/docs/installation_integration/html/* %{buildroot}%{_pkgdocdir}/installation_integration
cp -a %{_vpath_builddir}/docs/notes/html/* %{buildroot}%{_pkgdocdir}/notes
cp -a %{_vpath_builddir}/docs/sdk/html/* %{buildroot}%{_pkgdocdir}/sdk
find %{buildroot}%{_pkgdocdir} -type d -print0 | xargs -0 chmod -c 0755
find %{buildroot}%{_pkgdocdir} -type f -print0 | xargs -0 chmod -c 0644
find %{buildroot}%{_pkgdocdir} -type f -name '.*' -delete -print
hardlink -cfv %{buildroot}%{_pkgdocdir}

# Find installed icons.
find %{buildroot}%{_datadir}/icons/hicolor -type f -print | \
sed -e 's!^%{buildroot}!!g' > %{lc_name}.icons

# Find translation files.
%if !(0%{?qt6_build})
%find_lang %{lc_name} --with-qt
%endif


%check
%ctest
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.rst
%license AUTHORS
%license LICENSE.en.txt
%license LICENSE.txt
%{_bindir}/.%{newname}.hmac
%{_bindir}/%{newname}
%{_datadir}/applications/com.governikus.%{lc_name}.desktop
%{_libexecdir}/.%{newname}.hmac
%{_libexecdir}/%{newname}
%{_mandir}/man1/%{newname}.1*
%{_metainfodir}/com.governikus.%{lc_name}.metainfo.xml


%if 0%{?qt6_build}
%files data -f %{lc_name}.icons
%else
%files data -f %{lc_name}.icons -f %{lc_name}.lang
%endif
%{_datadir}/%{newname}


%files doc
%doc %{_pkgdocdir}
%license %{_licensedir}/%{name}*


%changelog
%autochangelog
