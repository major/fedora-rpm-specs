Name:           python-zopeundo
Version:        5.0
Release:        1%{?dist}
Summary:        ZODB undo support for Zope
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/ZopeUndo
Source0:        %{url}/archive/%{version}/ZopeUndo-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist docutils}

%description
This package is used to support the Prefix object that Zope 2 uses for
the undo log.  It is a separate package only to aid configuration
management.

This package is included in Zope 2.  It can be used in a ZEO server to
allow it to support Zope 2's undo log, without pulling in all of Zope 2.

%package     -n python3-zopeundo
Summary:        %{summary}

%description -n python3-zopeundo
This package is used to support the Prefix object that Zope 2 uses for
the undo log.  It is a separate package only to aid configuration
management.

This package is included in Zope 2.  It can be used in a ZEO server to
allow it to support Zope 2's undo log, without pulling in all of Zope 2.

%prep
%autosetup -n ZopeUndo-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel
rst2html --no-datestamp CHANGES.rst CHANGES.html
rst2html --no-datestamp README.rst README.html

%install
%pyproject_install
%pyproject_save_files ZopeUndo

%check
export PYTHONPATH=%{buildroot}%{python3_sitelib}
zope-testrunner --test-path=src

%files -n python3-zopeundo -f %{pyproject_files}
%doc CHANGES.html README.html
%license COPYRIGHT.txt LICENSE.txt

%changelog
* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 5.0-1
- Dynamically generate BuildRequires

* Mon Jan 23 2023 Jerry James <loganjerry@gmail.com> - 5.0-1
- Initial RPM
