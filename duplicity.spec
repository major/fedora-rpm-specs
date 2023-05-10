%bcond_without check

Name:           duplicity
Version:        1.2.2
Release:        %autorelease
Summary:        Encrypted bandwidth-efficient backup using rsync algorithm

# The entire source is GPL-2.0-or-later, except:
#
# MIT:
#   - duplicity/backends/b2backend.py
#   - duplicity/backends/pyrax_identity/hubic.py
# GPL-3.0-or-later:
#   - duplicity/backends/tahoebackend.py
#
# Additionally, the following are not installed and therefore do not contribute
# to the license of the binary RPM:
#
# LGPL-2.1-or-later:
#   - testing/unit/test_gpginterface.py:
License:        GPL-2.0-or-later AND MIT AND GPL-3.0-or-later
URL:            https://duplicity.gitlab.io/
Source0:        https://launchpad.net/duplicity/1.0/%{version}/+download/duplicity-%{version}.tar.gz
Source1:        https://launchpad.net/duplicity/1.0/%{version}/+download/duplicity-%{version}.tar.gz.sig
# Trust on first use: keyring created on 2022-12-13 with:
#   workdir="$(mktemp --directory)"
#   gpg2 --with-fingerprint duplicity-1.2.1.tar.gz.sig 2>&1 |
#     awk '$2 == "using" { print "0x" $NF }' |
#     xargs gpg2 --homedir="${workdir}" \
#         --keyserver=hkps://keyserver.ubuntu.com --recv-keys
#   gpg2 --homedir="${workdir}" --export --export-options export-minimal \
#       > duplicity.gpg
#   rm -rf "${workdir}"
# Inspect keys using:
#   gpg2 --list-keys --no-default-keyring --keyring ./duplicity.gpg
# Contains:
#   8B6F8FF4E654E600: public key "Duplicity Test (no password) <duplicity@loafman.com>"
# The key name does not inspire confidence, but it is better than nothing!
Source2:        duplicity.gpg
# chg:test: Add test case for issue #683.
# https://gitlab.com/duplicity/duplicity/-/commit/e6671cdf4ed8b21b4a8bd1973bd458f62792cd29
Patch0:         e6671cdf4ed8b21b4a8bd1973bd458f62792cd29.patch

Requires:       ca-certificates
Requires:       gnupg >= 1.0.6
Requires:       python3dist(pexpect)
Requires:       rsync

Recommends:     ncftp >= 3.1.9
Recommends:     openssh-clients
Recommends:     python3dist(PyDrive2)
Recommends:     python3dist(boto3)
Recommends:     python3dist(dropbox)
Recommends:     python3dist(paramiko)

# For verifying the source archive signature:
BuildRequires:  gnupg2

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  librsync-devel >= 0.9.6
BuildRequires:  python3dist(wheel)
# dependencies for check
BuildRequires:  gnupg >= 1.0.6
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(fasteners)
BuildRequires:  python3dist(future)
BuildRequires:  python3dist(pexpect)
BuildRequires:  python3dist(pytest)

%description
Duplicity incrementally backs up files and directory by encrypting
tar-format volumes with GnuPG and uploading them to a remote (or
local) file server. In theory many protocols for connecting to a
file server could be supported; so far ssh/scp, local file access,
rsync, ftp, HSI, WebDAV and Amazon S3 have been written.

Because duplicity uses librsync, the incremental archives are space
efficient and only record the parts of files that have changed since
the last backup. Currently duplicity supports deleted files, full
unix permissions, directories, symbolic links, fifos, device files,
but not hard links.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files duplicity

mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
ln -sf %{_sysconfdir}/pki/tls/cert.pem \
       %{buildroot}/%{_sysconfdir}/%{name}/cacert.pem

%find_lang %{name}

# drop documentation
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/AUTHORS
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/CHANGELOG.md
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/COPYING
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/README.md
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/README-LOG.md
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/README-TESTING.md
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/README-REPO.md
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/CONTRIBUTING.md

%if %{with check}
%check
%pytest
%endif

%files -f %{name}.lang -f %{pyproject_files}
# pyproject_files handles COPYING in dist-info; verify with “rpm -qL -p …”
%doc CHANGELOG.md README.md CONTRIBUTING.md
%{_bindir}/rdiffdir
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_mandir}/man1/rdiffdir*
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/cacert.pem

%changelog
%autochangelog
