Name:           python-zc-lockfile
Version:        4.1
Release:        %autorelease
Summary:        Basic Inter-Process Locks
License:        ZPL-2.1
URL:            https://pypi.org/project/zc.lockfile/
Source0:        %{pypi_source zc_lockfile}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-zope-testing
BuildRequires:  python3-zope-testrunner

%global _description\
The zc.lockfile package provides a basic portable implementation of\
interprocess locks using lock files. The purpose if not specifically\
to lock files, but to simply provide locks with an implementation based\
on file-locking primitives. Of course, these locks could be used to\
mediate access to other files. For example, the ZODB file storage\
implementation uses file locks to mediate access to file-storage\
database files. The database files and lock file files are separate files.

%description %_description

%package -n python3-zc-lockfile
Summary:        Basic Inter-Process Locks

%description -n python3-zc-lockfile
The zc.lockfile package provides a basic portable implementation of
interprocess locks using lock files. The purpose if not specifically
to lock files, but to simply provide locks with an implementation based
on file-locking primitives. Of course, these locks could be used to
mediate access to other files. For example, the ZODB file storage
implementation uses file locks to mediate access to file-storage
database files. The database files and lock file files are separate files.

%prep
%setup -q -n zc_lockfile-%{version}
# Drop upstream's setuptools upper bound; Fedora ships newer setuptools
sed -Ei 's/(setuptools >= [0-9.]+), *< *[0-9.]+/\1/' pyproject.toml tox.ini

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files zc

%check
%tox

%files -n python3-zc-lockfile -f %{pyproject_files}
%doc CHANGES.rst src/zc/lockfile/README.rst
%license LICENSE.txt


%changelog
%autochangelog
