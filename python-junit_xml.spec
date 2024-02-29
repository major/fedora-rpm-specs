# Upstream does not tag releases on GitHub (and did not upload a source archive
# to PyPI for version 1.9).
%global commit ba89b41638df8ad2011c2818672f208a91a5a4a0
%global snapdate 20200222

Name:           python-junit_xml
Summary:        Python module for creating JUnit XML test result documents
Version:        1.9^%{snapdate}git%{sub %{commit} 1 7}
Release:        %autorelease

# SPDX
License:        MIT
URL:            https://github.com/kyrus/python-junit-xml
Source:         %{url}/archive/%{commit}/python-junit-xml-%{commit}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global common_description %{expand:
A Python module for creating JUnit XML test result documents that can be read
by tools such as Jenkins or Bamboo. If you are ever working with test tool or
test suite written in Python and want to take advantage of Jenkins’ or Bamboo’s
pretty graphs and test reporting capabilities, this module will let you
generate the XML test reports.}

%description %{common_description}


%package -n python3-junit-xml
Summary:        %{summary}

# The source package is named python-junit_xml for historical reasons.  The
# binary package, python3-junit-xml, is named using the canonical project
# name[1]; see also [2].
#
# The %%py_provides macro is used to provide an upgrade path from
# python3-junit_xml and to produce the appropriate Provides for the importable
# module[3].
#
# [1] https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_canonical_project_name
# [2] https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_library_naming
# [3] https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_provides_for_importable_modules

# Provide an upgrade path
%py_provides python3-junit_xml
Obsoletes:      python3-junit_xml < 1.9^20200222gitba89b41-8

%description -n python3-junit-xml %{common_description}


%prep
%autosetup -n python-junit-xml-%{commit}
# Remove shebang line in non-script source
sed -r -i '1{/^#!/d}' junit_xml/__init__.py


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l junit_xml


%check
%tox


%files -n python3-junit-xml -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
