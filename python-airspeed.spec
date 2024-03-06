%global forgeurl https://github.com/purcell/airspeed

Name:           python-airspeed
Version:        0.6.0
Release:        %autorelease
Summary:        A lightweight template engine compatible with Velocity
%global tag %{version}
%forgemeta
License:        BSD-2-Clause
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Airspeed is a powerful and easy-to-use templating engine for Python that aims
for a high level of compatibility with the popular Velocity library for Java.

 • Compatible with Velocity templates
 • Compatible with Python 2.6 and greater, including Jython
 • Features include macros definitions, conditionals, sub-templates and much
   more
 • Airspeed is already being put to serious use
 • Comprehensive set of unit tests; the entire library was written test-first
 • Reasonably fast
 • A single Python module of a few kilobytes, and not the 500kb of Velocity
 • Liberal license (BSD-style)}

%description %_description


%package -n python3-airspeed
Summary:        %{summary}

%description -n python3-airspeed %_description


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l airspeed


%check
%{py3_test_envvars} %{python3} -m unittest tests

%files -n python3-airspeed -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
