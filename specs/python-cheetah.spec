Name:           python-cheetah
Version:        3.4.0
Release:        %autorelease
Summary:        Template engine and code generator

# Most source code is MIT, except:
# BSD-3-Clause-HP:
#   Cheetah/c/_namemapper.h
# LGPL-2.1-or-later:
#   Cheetah/Utils/statprof.py
# LicenseRef-Fedora-Public-Domain:
#   Cheetah/Tests/xmlrunner.py
License:        MIT AND BSD-3-Clause-HP AND LGPL-2.1-or-later AND LicenseRef-Fedora-Public-Domain
URL:            https://cheetahtemplate.org/
Source:         https://github.com/CheetahTemplate3/cheetah3/archive/%{version}/cheetah3-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  python3-devel

%global _description %{expand:
Cheetah3 is a free and open source template engine and code generation tool.
It can be used standalone or combined with other tools and frameworks.  Web
development is its principle use, but Cheetah is very flexible and is also
being used to generate C++ game code, Java, sql, form emails and even Python
code.}

%description %{_description}


%package -n python3-cheetah
Summary:        %{summary}


%description -n python3-cheetah %{_description}


%prep
%autosetup -p1 -n cheetah3-%{version}

# remove unnecessary shebang lines to silence rpmlint
find Cheetah -type f -name '*.py' -print0 | xargs -0 sed -i -e '1 {/^#!/d}'


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files Cheetah


%check
# changing this in %%prep would cause an rpmlint error (rpm-buildroot-usage),
# so do it here instead
sed -e 's|{envsitepackagesdir}|%{buildroot}%{python3_sitearch}|' -i tox.ini
%tox


%files -n python3-cheetah -f %{pyproject_files}
%doc ANNOUNCE.rst README.rst LATEST-CHANGES.rst BUGS
%{_bindir}/cheetah*


%changelog
%autochangelog
