%bcond_without check

Name:           duplicity
Version:        3.0.3.2
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
#Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source0:        https://gitlab.com/duplicity/duplicity/-/archive/rel.%{version}/duplicity-rel.%{version}.tar.bz2
# chg:test: Add test case for issue #683.
# https://gitlab.com/duplicity/duplicity/-/commit/e6671cdf4ed8b21b4a8bd1973bd458f62792cd29
Patch0:         e6671cdf4ed8b21b4a8bd1973bd458f62792cd29.patch

Requires:       ca-certificates
Requires:       gnupg >= 1.0.6
Requires:       python3dist(pexpect)
Requires:  python3dist(fasteners)
Requires:       rsync

Recommends:     ncftp >= 3.1.9
Recommends:     openssh-clients
Recommends:     python3dist(boto3)
Recommends:     python3dist(dropbox)
Recommends:     python3dist(paramiko)

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
%autosetup -p1 -n %{name}-rel.%{version}

# Unset all the python module pins
sed -i "s/==.*$//g" requirements.txt
sed -i "s/<.*$//g" requirements.txt
sed -i "s/>=.[^\s][^,][^\"]*//g" pyproject.toml
sed -i /pipx/d pyproject.toml

# Strip requirements on optional modules not in Fedora
for i in atom boxsdk gdata-python3 gettext jottalib mediafire megatools pyrax pydrive2; do
  sed -i /"$i"/d requirements.txt
done

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
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/AUTHORS.md
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/CHANGELOG.md
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/COPYING
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/README.md
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/README-LOG.md
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/README-SNAP.md
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/README-TESTING.md
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/README-REPO.md

%if %{with check}
# https://gitlab.com/duplicity/duplicity/-/issues/820
%ifnarch ppc64le
%check
%pytest
%endif
%endif

%files -f %{name}.lang -f %{pyproject_files}
# pyproject_files handles COPYING in dist-info; verify with “rpm -qL -p …”
%doc AUTHORS.md CHANGELOG.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/cacert.pem

%changelog
%autochangelog
