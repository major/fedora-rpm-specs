# Upstream does not tag releases on GitHub (and did not upload a source archive
# to PyPI for version 1.9).
%global commit ba89b41638df8ad2011c2818672f208a91a5a4a0
%global snapdate 20200222

Name:           python-junit_xml
Summary:        Python module for creating JUnit XML test result documents
Version:        1.9^%{snapdate}git%(echo '%{commit}' | cut -b -7)
Release:        %autorelease

# SPDX
License:        MIT
URL:            https://github.com/kyrus/python-junit-xml
Source0:        %{url}/archive/%{commit}/python-junit-xml-%{commit}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global common_description %{expand:
A Python module for creating JUnit XML test result documents that can be read
by tools such as Jenkins or Bamboo. If you are ever working with test tool or
test suite written in Python and want to take advantage of Jenkins’ or Bamboo’s
pretty graphs and test reporting capabilities, this module will let you
generate the XML test reports.}

%description %{common_description}


%package -n python3-junit_xml
Summary:        %{summary}

%py_provides python3-junit-xml

%description -n python3-junit_xml %{common_description}


%prep
%autosetup -n python-junit-xml-%{commit} -p1


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files junit_xml


%check
%tox


%files -n python3-junit_xml -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
