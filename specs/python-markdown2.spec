%global srcname markdown2

Name:           python-%{srcname}
Version:        2.5.4
Release:        %autorelease
Summary:        A fast and complete Python implementation of Markdown
License:        MIT
URL:            https://github.com/trentm/python-%{srcname}/
Source0:        https://pypi.io/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Markdown is a text-to-HTML filter; it translates an easy-to-read /
easy-to-write structured text format into HTML. Markdown's text format
is most similar to that of plain text email, and supports features
such as headers, emphasis, code blocks, blockquotes, and links.

This is a fast and complete Python implementation of the Markdown
spec.

For information about markdown itself, see
http://daringfireball.net/projects/markdown/}

%description %_description


%package -n python3-%{srcname}
Summary:        A fast and complete Python implementation of Markdown

%description -n python3-%{srcname} %_description


# other dependencies (latex2mathml, wavedrom) not packaged
%pyproject_extras_subpkg -n python3-%{srcname} code_syntax_highlighting


%prep
%autosetup -n %{srcname}-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

# remove shebangs and fix permissions
find %{buildroot}%{python3_sitelib} \
  \( -name '*.py' -o -name 'py.*' \) \
  -exec sed -i '1{/^#!/d}' {} \; \
  -exec chmod u=rw,go=r {} \;

%pyproject_save_files -l %{srcname}


%check
%pyproject_check_import

pushd test
%{__python3} test.py -- -knownfailure %{?skip_tests} || :
popd


%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGES.md
%doc CONTRIBUTORS.txt
%doc TODO.txt
%{_bindir}/%{srcname}


%changelog
%autochangelog
