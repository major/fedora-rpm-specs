# Note that `copyparty` vendors Python, Javascript, CSS, and font files in
# its upstream releases. Together with upstream we've been able to de-vendor
# the Python dependencies but the Javascript and CSS is difficult to undo.
# These files are either not packaged in Fedora, or are patched upstream [1].

# This package skips trying to de-vendor these assets under the 'hardship' part
# of the Javascript packaging policy [2] or the similar clause under the CSS
# packaging guidelines [3].
#
# > Packages containing JavaScript should make the best effort to regenerate
# > any precompiled/minimized JS wherever possible, as this leads to more
# > maintainable packages. Where this would result in a significant hardship,
# > the bundled pregenerated JS may be shipped with a specfile comment
# > explaining the decision. This does not eliminate the requirement to
# > validate licenses of bundled code.
#
# Licenses for the vendored javascript have been separately verified and are
# included in the `License` field.
#
# [1]: https://github.com/9001/copyparty/issues/887#issuecomment-3368299632
# [2]: https://docs.fedoraproject.org/en-US/packaging-guidelines/JavaScript/
# [3]: https://docs.fedoraproject.org/en-US/packaging-guidelines/Web_Assets/#_css

Name:           copyparty
Version:        1.20.21
Release:        1%{?dist}
Summary:        Portable file server with many supported protocols

# Licenses include both `copyparty` itself and vendored javascript libraries
# and font files where applicable.
License:        MIT AND Apache-2.0 AND OFL-1.1
URL:            https://github.com/9001/copyparty
Source:         %{url}/releases/download/v%{version}/copyparty-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)


Requires:       python3dist(qrcodegen)
Requires:       python3dist(ifaddr)
Requires:       python3dist(dnslib)

# Test requirements are generally the same as those needed
# for runtime.
BuildRequires:  python3dist(qrcodegen)

# On-the-fly certificate generation when available
Recommends:     golang-github-cloudflare-cfssl

# Thumbnailing, media indexing, and audio transcoding functionality
Recommends:     python3-pillow
Recommends:     ffmpeg

%global _description %{expand:
Portable file server with accelerated resumable uploads, deduplication, WebDAV,
FTP,zeroconf, media indexer, video thumbnails, audio transcoding, and write-only
folders
}

%description %_description

%package -n copyparty-u2c
Requires: copyparty

Summary: The upload2copyparty client application

%description -n copyparty-u2c %_description

%package -n copyparty-partyfuse
Requires: copyparty
Requires: python3dist(fusepy)

Summary: Mount a copyparty instance through FUSE

%description -n copyparty-partyfuse %_description

%prep
%autosetup -p1 -n copyparty-%{version}

# Upstream vendors certain Python libraries but has made it possible in the
# 1.19.16 release [1] to unvendor them. Let's do that.
# [1]: https://github.com/9001/copyparty/releases/tag/v1.19.16

# Only vendored for size see [1]
# [1]: https://github.com/9001/copyparty/issues/887#issuecomment-3368299632
rm -rf copyparty/stolen/qrcodegen.py

# Only vendored for Python 2 support, see [1]
# [1]: https://github.com/9001/copyparty/issues/887#issuecomment-3368299632
rm -rf copyparty/stolen/surrogateescape.py

# Only vendored (and upstream patched) for Python 2 support, see [1]
# [1]: https://github.com/9001/copyparty/issues/887#issuecomment-3368299632
rm -rf copyparty/stolen/ifaddr

# Vendored (and upstream patched) for an Avahi bug, see [1]
# [1]: https://github.com/9001/copyparty/issues/887#issuecomment-3368299632
rm -rf copyparty/stolen/dnslib

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files copyparty

%check
%pytest

%files -n copyparty -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/copyparty

%files -n copyparty-u2c
%{_bindir}/u2c

%files -n copyparty-partyfuse
%{_bindir}/partyfuse

%changelog
* Fri Aug 28 2026 Simon de Vlieger <cmdr@supakeen.com> - 1.20.21-1
- Initial build
