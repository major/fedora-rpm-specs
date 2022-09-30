%bcond_without check

Name:           duplicity
Version:        1.0.0
Release:        %autorelease
Summary:        Encrypted bandwidth-efficient backup using rsync algorithm

License:        GPLv2+
URL:            http://www.nongnu.org/duplicity/
Source0:        https://launchpad.net/duplicity/1.0/%{version}/+download/duplicity-%{version}.tar.gz

Requires:       ca-certificates
Requires:       gnupg >= 1.0.6
Requires:       python3dist(lockfile)
Requires:       python3dist(pexpect)
Requires:       rsync

Recommends:     ncftp >= 3.1.9
Recommends:     openssh-clients
Recommends:     python3dist(PyDrive2)
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
BuildRequires:  python3dist(future)
BuildRequires:  python3dist(pexpect)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-runner)


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
%autosetup -p0

%generate_buildrequires
%pyproject_buildrequires

%build
%py3_build

%install
%py3_install

mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
ln -sf %{_sysconfdir}/pki/tls/cert.pem \
       %{buildroot}/%{_sysconfdir}/%{name}/cacert.pem

%find_lang %{name}

# drop documentation
rm -rf    %{buildroot}%{_docdir}/duplicity-%{version}/AUTHORS
rm -rf    %{buildroot}%{_docdir}/duplicity-%{version}/CHANGELOG.md
rm -rf    %{buildroot}%{_docdir}/duplicity-%{version}/COPYING
rm -rf    %{buildroot}%{_docdir}/duplicity-%{version}/README.md
rm -rf    %{buildroot}%{_docdir}/duplicity-%{version}/README-LOG.md
rm -rf    %{buildroot}%{_docdir}/duplicity-%{version}/README-TESTING.md
rm -rf    %{buildroot}%{_docdir}/duplicity-%{version}/README-REPO.md
rm -rf    %{buildroot}%{_docdir}/duplicity-%{version}/CONTRIBUTING.md

%if %{with check}
%check
%pytest
%endif

%files -f %{name}.lang
%license COPYING
%doc CHANGELOG.md README.md CONTRIBUTING.md
%{_bindir}/rdiffdir
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_mandir}/man1/rdiffdir*
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/cacert.pem
%{python3_sitearch}/duplicity/
%{python3_sitearch}/duplicity-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
