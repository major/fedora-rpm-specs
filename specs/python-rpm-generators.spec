Name:           python-rpm-generators
Summary:        Dependency generators for Python RPMs
Version:        14
Release:        %autorelease

Url:            https://src.fedoraproject.org/rpms/python-rpm-generators

# Originally the following files were part of RPM, so the license is inherited: GPL-2.0-or-later
# The COPYING file is grabbed from the last commit that changed the files
Source0:        https://raw.githubusercontent.com/rpm-software-management/rpm/102eab50b3d0d6546dfe082eac0ade21e6b3dbf1/COPYING
Source1:        python.attr
Source2:        pythondist.attr
# This was crafted in-place as a fork of python.attr, hence also GPL-2.0-or-later
Source3:        pythonname.attr
# This one is also originally from RPM, but it has its own license declaration: LGPL-2.1-or-later
Source4:        pythondistdeps.py
# This was crafted in-place with the following license declaration:
#  LicenseRef-Fedora-Public-Domain OR CC0-1.0 OR LGPL-2.1-or-later OR GPL-2.0-or-later
# Note that CC0-1.0 is not allowed for code in Fedora, so we skip it in the package License tag
Source5:        pythonbundles.py

# See individual licenses above Source declarations
# Originally, this was simplified to GPL-2.0-or-later, but "effective license" analysis is no longer allowed
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND (LicenseRef-Fedora-Public-Domain OR LGPL-2.1-or-later OR GPL-2.0-or-later)

BuildArch:      noarch

%description
%{summary}.

%package -n python3-rpm-generators
Summary:        %{summary}
Requires:       python3-packaging
# We have parametric macro generators, we need RPM 4.16 (4.15.90+ is 4.16 alpha)
Requires:       rpm > 4.15.90-0
# This contains the Lua functions we use:
Requires:       python-srpm-macros >= 3.10-15

%description -n python3-rpm-generators
%{summary}.

%prep
%autosetup -c -T
cp -a %{sources} .

%install
install -Dpm0644 -t %{buildroot}%{_fileattrsdir} *.attr
install -Dpm0755 -t %{buildroot}%{_rpmconfigdir} *.py

%files -n python3-rpm-generators
%license COPYING
%{_fileattrsdir}/python.attr
%{_fileattrsdir}/pythondist.attr
%{_fileattrsdir}/pythonname.attr
%{_rpmconfigdir}/pythondistdeps.py
%{_rpmconfigdir}/pythonbundles.py

%changelog
%autochangelog
