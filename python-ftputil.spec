Name:           python-ftputil
Version:        5.1.0
Release:        %autorelease
Summary:        High-level FTP client library (virtual file system and more)

# The entire source is BSD-3-Clause, except ftputil/lrucache.py, which is (BSD-3-Clause OR AFL-2.1)
License:        BSD-3-Clause AND (BSD-3-Clause OR AFL-2.1)
URL:            https://ftputil.sschwarzer.net/
# Bug tracker: https://todo.sr.ht/~sschwarzer/ftputil
# Git hosting: https://git.sr.ht/~sschwarzer/ftputil
Source:         %{pypi_source ftputil}

BuildArch:      noarch

BuildRequires:  python3-devel
# There is no list of test dependencies anywhere in the PyPI sdist. We could
# use an archive from https://git.sr.ht/~sschwarzer/ftputil, but it’s easier
# just to list them manually:
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist freezegun}
# For /usr/bin/ftp:
BuildRequires:  ftp

%global common_description %{expand:
ftputil is a high-level FTP client library for the Python programming language.
ftputil implements a virtual file system for accessing FTP servers, that is, it
can generate file-like objects for remote files. The library supports many
functions similar to those in the os, os.path and shutil modules. ftputil has
convenience functions for conditional uploads and downloads, and handles FTP
clients and servers in different timezones.}

%description %{common_description}


%package -n python3-ftputil
Summary:        %{summary}

# The file ftputil/lrucache.py is a bundled copy of
# https://pypi.org/project/lrucache/; it cannot reasonably be unbundled because
# the original project is defunct (last upstream release in 2004). The version
# number is based on a comment in the source file.
Provides:       bundled(python3dist(lrucache)) = 0.2

Requires:       ftp

%description -n python3-ftputil %{common_description}


%prep
%autosetup -n ftputil-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l ftputil


%check
# These tests require a real FTP server.
ignore="${ignore-} --ignore=test/test_real_ftp.py"

# This requires network access:
k="${k-}${k+ and }not (TestPublicServers and test_servers)"

# Required for TestAcceptEitherUnicodeOrBytes.test_upload, but not included in
# the PyPI sdist. This doesn’t need to be a real Makefile; it just needs to
# exist.
touch Makefile

%pytest ${ignore-} -k "${k-}" -v


%files -n python3-ftputil -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
