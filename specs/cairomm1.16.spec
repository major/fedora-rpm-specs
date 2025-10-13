%global so_version 1
%global apiver 1.16

# “Let mm-common-get copy some files to untracked/”, i.e., replace scripts from
# the tarball with those from mm-common. This is (potentially) required if
# building an autotools-generated tarball with meson, or vice versa.
%bcond maintainer_mode 1

Name:           cairomm%{apiver}
Summary:        C++ API for the cairo graphics library
Version:        1.18.0
Release:        %autorelease

URL:            https://www.cairographics.org
License:        LGPL-2.0-or-later
# The following files under other allowable licenses belong to the build system
# and do not contribute to the licenses of the binary RPMs.
#
# FSFAP:
#   build/ax_boost_base.m4
#   build/ax_boost_test_exec_monitor.m4
#   build/ax_boost_unit_test_framework.m4
# GPL-2.0-or-later:
#   untracked/docs/tagfile-to-devhelp2.xsl
# LGPL-2.1-or-later:
#   Makefile.am
#   cairomm/Makefile.am
#   configure.ac
#   docs/Makefile.am
# MIT:
#   untracked/docs/reference/html/dynsections.js
#   untracked/docs/reference/html/jquery.js
#   untracked/docs/reference/html/menu.js
#   untracked/docs/reference/html/menudata.js
SourceLicense:  %{shrink:
                %{license} AND
                FSFAP AND
                GPL-2.0-or-later AND
                LGPL-2.1-or-later AND
                MIT
                }

%global src_base https://www.cairographics.org/releases
Source0:        %{src_base}/cairomm-%{version}.tar.xz
# No keyring with authorized GPG signing keys is published
# (https://gitlab.freedesktop.org/freedesktop/freedesktop/-/issues/331), but we
# are able to verify the signature using the key for Kjell Ahlstedt from
# https://gitlab.freedesktop.org/freedesktop/freedesktop/-/issues/290.
Source1:        %{src_base}/cairomm-%{version}.tar.xz.asc
Source2:        https://gitlab.freedesktop.org/freedesktop/freedesktop/uploads/0ac64e9582659f70a719d59fb02cd037/gpg_key.pub

# Fix outdated FSF mailing address in COPYING
# https://gitlab.freedesktop.org/cairo/cairomm/-/merge_requests/29
# (Merged upstream, so we are comfortable patching the license file.)
Patch:          https://gitlab.freedesktop.org/cairo/cairomm/-/merge_requests/29.patch
# Change license info to mention Lesser GPL 2.1 instead of Library GPL 2
#
# The GNU Library General Public License has been superseded by
# the GNU Lesser General Public License.
# https://www.gnu.org/licenses/old-licenses/lgpl-2.0.html
#
# Remove obsolete FSF (Free Software Foundation) address.
# Committed to master branch:
# https://gitlab.freedesktop.org/cairo/cairomm/-/commit/43580ed75bde0b7d6ad442c90a22f80b50ce844d
Patch:          https://gitlab.freedesktop.org/cairo/cairomm/-/commit/43580ed75bde0b7d6ad442c90a22f80b50ce844d.patch

BuildRequires:  gnupg2

BuildRequires:  gcc-c++
BuildRequires:  meson

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(sigc++-3.0)
BuildRequires:  pkgconfig(fontconfig)

# Everything mentioned in data/cairomm*.pc.in, except the Quartz and Win32
# libraries that do not apply to this platform:
BuildRequires:  pkgconfig(cairo-ft)
BuildRequires:  pkgconfig(cairo-pdf)
BuildRequires:  pkgconfig(cairo-png)
BuildRequires:  pkgconfig(cairo-ps)
BuildRequires:  pkgconfig(cairo-svg)
BuildRequires:  pkgconfig(cairo-xlib)
BuildRequires:  pkgconfig(cairo-xlib-xrender)

%if %{with maintainer_mode}
# mm-common-get
BuildRequires:  mm-common >= 1.0.4
%endif

BuildRequires:  doxygen
# dot
BuildRequires:  graphviz
# xsltproc
BuildRequires:  libxslt
BuildRequires:  pkgconfig(mm-common-libstdc++)

# For tests:
BuildRequires:  boost-devel

%description
This library provides a C++ interface to cairo.

The API/ABI version series is %{apiver}.


%package        devel
Summary:        Development files for cairomm%{apiver}
Requires:       cairomm%{apiver}%{?_isa} = %{version}-%{release}

%description    devel
The cairomm%{apiver}-devel package contains libraries and header files for
developing applications that use cairomm%{apiver}.

The API/ABI version series is %{apiver}.


%package        doc
Summary:        Documentation for cairomm%{apiver}

# We unbundle Doxygen-inserted JavaScript assets from the HTML documentation
# as much as possible, as prescribed in
# https://src.fedoraproject.org/rpms/doxygen/blob/f42/f/README.rpm-packaging.
#
# Some files originating in Doxygen are still bundled or are generated from
# templates specifically for this package; where these have explicitly
# documented licenses, they are MIT.
License:        %{license} AND MIT

BuildArch:      noarch

%{?doxygen_js_requires}

%description    doc
Documentation for cairomm%{apiver} can be viewed through the devhelp
documentation browser.

The API/ABI version series is %{apiver}.


%prep
%{gpgverify} \
    --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -n cairomm-%{version} -p1

# Remove the tag file, which triggers a rebuild of the documentation.
# While we are at it, we might as well rebuild the devhelp XML too.
rm -rf untracked/docs/reference/html
rm untracked/docs/reference/cairomm-%{apiver}.tag \
   untracked/docs/reference/cairomm-%{apiver}.devhelp2


%conf
%meson \
  -Dmaintainer-mode=%{?with_maintainer_mode:true}%{?!with_maintainer_mode:false} \
  -Dbuild-documentation=true \
  -Dbuild-examples=false \
  -Dbuild-tests=true \
  -Dboost-shared=true \
  -Dwarnings=max


%build
%meson_build


%install
%meson_install

install -t %{buildroot}%{_docdir}/cairomm-%{apiver} -m 0644 -p \
    ChangeLog NEWS README.md
cp -rp examples %{buildroot}%{_docdir}/cairomm-%{apiver}/

%{doxygen_unbundle_buildroot}


%check
%meson_test


%files
%license COPYING
%{_libdir}/libcairomm-%{apiver}.so.%{so_version}{,.*}


%files devel
%{_includedir}/cairomm-%{apiver}/
%{_libdir}/libcairomm-%{apiver}.so
%{_libdir}/pkgconfig/cairomm-%{apiver}.pc
%{_libdir}/pkgconfig/cairomm-*-%{apiver}.pc
%{_libdir}/cairomm-%{apiver}/


%files doc
%license COPYING
%doc %{_docdir}/cairomm-%{apiver}/
%doc %{_datadir}/devhelp/


%changelog
%autochangelog
