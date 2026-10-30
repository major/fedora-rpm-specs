%global commit d3936cf87339c70bf28204eafb7a1f4726828c5c
%global shortcommit %{sub %{commit} 0 7}
%global snapdate 20261028
# Unity is not packaged in Fedora and upstream's meson wrap would download
# it during the build. Ship the test framework sources for %check instead.
# Unity is test-only and never installed, so no Provides: bundled(unity)
# is required.
%global unity_commit bbf8f3728a937c7627b8094de7ae13559d220ed5

Name:           httpdirfs
Version:        1.3.3^%{snapdate}git%{shortcommit}
Release:        %autorelease
Summary:        Mount HTTP directory listings as a virtual filesystem

License:        GPL-3.0-or-later WITH sqlitestudio-OpenSSL-exception
URL:            https://github.com/fangfufu/httpdirfs
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1:        https://github.com/ThrowTheSwitch/Unity/archive/%{unity_commit}/Unity-%{unity_commit}.tar.gz

# Leaf package: drop the i686 build.
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(gumbo)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(expat)
BuildRequires:  help2man
# for integration test in %check
BuildRequires:  fuse3

%description
HTTPDirFS is a FUSE filesystem that allows you to mount HTTP directory
listings, with a built-in persistent cache. It also supports
Airsonic/Subsonic servers. It uses libcurl for HTTP transfers, Gumbo for
HTML parsing, and FUSE3 for filesystem presentation.

%prep
%autosetup -n %{name}-%{commit} -a 1
# Fail early if upstream moved to a different Unity revision than the one
# bundled here; otherwise the tests would silently run against a stale
# framework.
unity_rev=
while read -r line; do
    if [[ $line =~ ^revision[[:space:]]*=[[:space:]]*([0-9a-f]{40}) ]]; then
        unity_rev=${BASH_REMATCH[1]}
        break
    fi
done < subprojects/unity.wrap
if [ "$unity_rev" != "%{unity_commit}" ]; then
    echo "ERROR: subprojects/unity.wrap pins Unity '${unity_rev:-<none>}'," \
         "but the spec bundles %{unity_commit}" >&2
    exit 1
fi
# Use the bundled Unity sources instead of the meson wrap, which would
# clone the framework from the network at configure time.
rm -f subprojects/unity.wrap subprojects/.wraplock
mv Unity-%{unity_commit} subprojects/unity

%build
%meson
%meson_build

%check
# The integration tests skip themselves when /dev/fuse is unavailable.
%meson_test

%install
%meson_install

%files
%license LICENSE
%doc README.md CHANGELOG.md docs/usage.md
%{_bindir}/httpdirfs
%{_mandir}/man1/httpdirfs.1*

%changelog
%autochangelog
