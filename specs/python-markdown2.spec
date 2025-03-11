%global srcname markdown2

Name:           python-%{srcname}
Version:        2.5.3
Release:        %autorelease
Summary:        A fast and complete Python implementation of Markdown
License:        MIT
URL:            https://github.com/trentm/python-%{srcname}/
Source0:        https://pypi.io/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pygments
BuildRequires:  python3-setuptools


%description
Markdown is a text-to-HTML filter; it translates an easy-to-read /
easy-to-write structured text format into HTML. Markdown's text format
is most similar to that of plain text email, and supports features
such as headers, emphasis, code blocks, blockquotes, and links.

This is a fast and complete Python implementation of the Markdown
spec.

For information about markdown itself, see
http://daringfireball.net/projects/markdown/


%package -n python3-%{srcname}
Summary:        A fast and complete Python implementation of Markdown
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Markdown is a text-to-HTML filter; it translates an easy-to-read /
easy-to-write structured text format into HTML. Markdown's text format
is most similar to that of plain text email, and supports features
such as headers, emphasis, code blocks, blockquotes, and links.

This is a fast and complete Python implementation of the Markdown
spec.

For information about markdown itself, see
http://daringfireball.net/projects/markdown/


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%py3_build


%install
%py3_install

# remove shebangs and fix permissions
find %{buildroot}%{python3_sitelib} \
  \( -name '*.py' -o -name 'py.*' \) \
  -exec sed -i '1{/^#!/d}' {} \; \
  -exec chmod u=rw,go=r {} \;


%check
pushd test
%{__python3} test.py -- -knownfailure %{?skip_tests} || :
popd


%files -n python3-%{srcname}
%doc CHANGES.md
%doc CONTRIBUTORS.txt
%doc TODO.txt
%license LICENSE.txt
%{python3_sitelib}/*
%exclude %dir %{python3_sitelib}/__pycache__
%{_bindir}/%{srcname}


%changelog
%autochangelog
