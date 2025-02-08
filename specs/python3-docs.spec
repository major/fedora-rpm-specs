Name:           python3-docs
Summary:        Documentation for the Python 3 programming language

# The Version should be in-sync with the python3 package:
%global         pybasever 3.13
%global         general_version %{pybasever}.2
#global         prerel ...
%global         upstream_version %{general_version}%{?prerel}
Version:        %{general_version}%{?prerel:~%{prerel}}
Release:        %autorelease
# The documentation is licensed as Python itself: Python-2.0.1
# Examples, recipes, and other code in the documentation are dual licensed under Python-2.0.1/0BSD
License:        Python-2.0.1 AND (Python-2.0.1 OR 0BSD)
URL:            https://www.python.org/
Source0:        %{url}ftp/python/%{general_version}/Python-%{upstream_version}.tar.xz
Source1:        %{url}ftp/python/%{general_version}/Python-%{upstream_version}.tar.xz.asc
# The release manager for Python 3.13 is Thomas Wouters
Source2: https://github.com/Yhg1s.gpg

# Fix bad link in documentation
Patch:   https://github.com/python/cpython/pull/129691.patch

BuildArch:      noarch

Recommends:     python3 = %{version}
%{?python_provide:%python_provide %{name}}

BuildRequires: make
BuildRequires:  %{__python3}
BuildRequires:  python3-docs-theme >= 2022.1
BuildRequires:  (python3-sphinx < 1:3 or python3-sphinx >= 1:3.2)
BuildRequires:  python3-docutils
BuildRequires:  python3-pygments
BuildRequires:  gnupg2

%bcond_without linkchecker
%if %{with linkchecker}
BuildRequires:  linkchecker
%endif


%description
The python3-docs package contains documentation on the Python 3
programming language and interpreter.

%prep
%gpgverify -k2 -s1 -d0
%autosetup -p1 -n Python-%{upstream_version}

%build
make -C Doc html PYTHON=%{__python3}
rm Doc/build/html/.buildinfo

%install
mkdir -p %{buildroot}

%check
# Verify that all of the local links work (see rhbz#670493 - doesn't apply
# to python3-docs, but only to older python-docs)
#
# (we can't check network links, as we shouldn't be making network connections
# within a build.  Also, don't bother checking the .txt source files; some
# contain example URLs, which don't work)
%if %{with linkchecker}
linkchecker \
  --ignore-url=^mailto: --ignore-url=^http --ignore-url=^ftp \
  --ignore-url=.txt\$ --no-warnings \
  Doc/build/html/index.html
%endif

%files
%doc Misc/NEWS Misc/HISTORY Misc/README Doc/build/html

%changelog
%autochangelog
