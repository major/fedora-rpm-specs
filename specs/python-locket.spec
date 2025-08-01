%global srcname locket

Name:           python-%{srcname}
Version:        1.0.0
Release:        %autorelease
Summary:        File-based locks for Python for Linux and Windows

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/mwilliamson/%{srcname}.py/
Source0:        https://github.com/mwilliamson/%{srcname}.py/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
# Use spur instaed of spur.local (which was a temporary name)
Patch:          https://github.com/mwilliamson/locket.py/pull/17.patch

%description
Locket implements a lock that can be used by multiple processes provided they
use the same path.

Locks largely behave as (non-reentrant) Lock instances from the threading
module in the standard library. Specifically, their behaviour is:

 * Locks are uniquely identified by the file being locked, both in the same
   process and across different processes.
 * Locks are either in a locked or unlocked state.
 * When the lock is unlocked, calling acquire() returns immediately and
   changes the lock state to locked.
 * When the lock is locked, calling acquire() will block until the lock state
   changes to unlocked, or until the timeout expires.
 * If a process holds a lock, any thread in that process can call release()
   to change the state to unlocked.
 * Behaviour of locks after fork is undefined.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        File-based locks for Python for Linux and Windows
BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{srcname}
Locket implements a lock that can be used by multiple processes provided they
use the same path.

Locks largely behave as (non-reentrant) Lock instances from the threading
module in the standard library. Specifically, their behaviour is:

 * Locks are uniquely identified by the file being locked, both in the same
   process and across different processes.
 * Locks are either in a locked or unlocked state.
 * When the lock is unlocked, calling acquire() returns immediately and
   changes the lock state to locked.
 * When the lock is locked, calling acquire() will block until the lock state
   changes to unlocked, or until the timeout expires.
 * If a process holds a lock, any thread in that process can call release()
   to change the state to unlocked.
 * Behaviour of locks after fork is undefined.


%prep
%autosetup -p1 -n %{srcname}.py-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pytest

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
