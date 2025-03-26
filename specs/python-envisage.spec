%global srcname envisage
#global commit 872c66885d64a22502fe3efceecec99c11a1c8ff
#global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{srcname}
Version:        7.0.3
Release:        %autorelease
Summary:        Extensible application framework

# Images have different licenses. For image license breakdown check
# image_LICENSE.txt file.
# All remaining source or image files are in BSD 3-clause license
License:        BSD-3-Clause AND LGPL-2.0-only AND CC-BY-SA-1.0 AND CC-BY-SA-2.5 AND CC-BY-SA-3.0 AND CC-BY-SA-4.0
URL:            https://github.com/enthought/envisage
Source0:        https://github.com/enthought/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
# For docs
BuildRequires:  python%{python3_pkgversion}-sphinx-copybutton
BuildRequires:  python%{python3_pkgversion}-enthought-sphinx-theme
# For tests
BuildRequires:  /usr/bin/xvfb-run

%description
Envisage is a Python-based framework for building extensible applications,
that is, applications whose functionality can be extended by adding
"plug-ins".  Envisage provides a standard mechanism for features to be added
to an application, whether by the original developer or by someone else.  In
fact, when you build an application using Envisage, the entire application
consists primarily of plug-ins.  In this respect, it is similar to the Eclipse
and Netbeans frameworks for Java applications.

Each plug-in is able to:

* Advertise where and how it can be extended (its "extension points").
* Contribute extensions to the extension points offered by other plug-ins.
* Create and share the objects that perform the real work of the application
  ("services").

The Envisage project provides the basic machinery of the plug-in framework as
well as GUI building tools (envisage.ui).  The workbench is the older way to
build GUIs from Envisage.  It is now recommended to use the Task framework. 


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Extensible application framework
BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{srcname}
Envisage is a Python-based framework for building extensible applications,
that is, applications whose functionality can be extended by adding
"plug-ins".  Envisage provides a standard mechanism for features to be added
to an application, whether by the original developer or by someone else.  In
fact, when you build an application using Envisage, the entire application
consists primarily of plug-ins.  In this respect, it is similar to the Eclipse
and Netbeans frameworks for Java applications.

Each plug-in is able to:

* Advertise where and how it can be extended (its "extension points").
* Contribute extensions to the extension points offered by other plug-ins.
* Create and share the objects that perform the real work of the application
  ("services").

The Envisage project provides the basic machinery of the plug-in framework as
well as GUI building tools (envisage.ui).  The workbench is the older way to
build GUIs from Envisage.  It is now recommended to use the Task framework. 


%package doc
Summary:        Documentation for %{name}
License:        BSD-3-Clause AND CC-BY-SA-1.0 AND CC-BY-SA-2.5 AND CC-BY-SA-3.0 AND CC-BY-SA-4.0

%description doc
Documentation and examples for %{name}


%prep
%autosetup -p1 -n %{srcname}-%{version}
# Fix line endings
sed -i -e 's/\r//' docs/source/envisage_core_documentation/*.rst
# Cleanup
find -name .gitignore -delete

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
xvfb-run %__python3 -m sphinx -b html docs/source docs/build
rm docs/build/.buildinfo
mv docs/build docs/html


%install
%pyproject_install
%pyproject_save_files %{srcname}
# Do not ship tests
find %{buildroot}%{python3_sitelib}/%{srcname} -name tests -type d -exec rm -r {} +
sed -i -e '\,/tests$,d' -e '\,/tests/,d' %{pyproject_files}


%check
xvfb-run %{__python3} -m unittest discover -v envisage

 
%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license *LICENSE*

%files doc
%license *LICENSE*
%doc docs/html examples


%changelog
%autochangelog
