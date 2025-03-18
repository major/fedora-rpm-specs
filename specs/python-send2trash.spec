%global pypiname Send2Trash

Name:           python-send2trash
Version:        1.8.3
Release:        %autorelease
Summary:        Python library to natively send files to Trash

License:        BSD-3-Clause
URL:            https://github.com/hsoft/send2trash

# PyPI sdist lacks tests
Source0:        %url/archive/%{version}/%{pypiname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description
Send2Trash is a small package that sends files to the Trash (or Recycle Bin)
natively and on all platforms. On OS X, it uses native FSMoveObjectToTrashSync
Cocoa calls, on Windows, it uses native (and ugly) SHFileOperation win32 calls.
On other platforms, if PyGObject and GIO are available, it will use this.
Otherwise, it will fallback to its own implementation of the trash specifications
from freedesktop.org.

%package -n python3-send2trash

Summary:        Python library to natively send files to Trash
Provides:       python3-%{pypiname} == %{version}-%{release}

%{?python_provide:%python_provide python3-%{pypiname}}
%{?python_provide:%python_provide python3-send2trash}

%description -n python3-send2trash
Send2Trash is a small package that sends files to the Trash (or Recycle Bin)
natively and on all platforms. On OS X, it uses native FSMoveObjectToTrashSync
Cocoa calls, on Windows, it uses native (and ugly) SHFileOperation win32 calls.
On other platforms, if PyGObject and GIO are available, it will use this.
Otherwise, it will fallback to its own implementation of the trash specifications
from freedesktop.org.

%generate_buildrequires
%pyproject_buildrequires

%prep
%setup -q -n send2trash-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files send2trash

%check
%pytest

%files -n python3-send2trash -f %{pyproject_files}
%doc README.rst CHANGES.rst
%{_bindir}/send2trash

%changelog
%autochangelog
