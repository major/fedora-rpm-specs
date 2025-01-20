%global         srcname         html-text
%global         forgeurl        https://github.com/zytedata/html-text
Version:        0.6.2
%global         tag             %{version}
%forgemeta

Name:           python-%{srcname}
Release:        2%{?dist}
Summary:        Extract text from HTML

License:        MIT
URL:            %{forgeurl}
Source:         %{forgeurl}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

BuildArch: noarch

%global _description %{expand:
How is html_text different from .xpath('//text()') from LXML
or .get_text() from Beautiful Soup?

- Text extracted with html_text does not contain inline styles,
javascript, comments and other text that is not normally visible
to users;

- html_text normalizes whitespace, but in a way smarter than
.xpath('normalize-space()), adding spaces around inline elements
(which are often used as block elements in html markup), and trying
to avoid adding extra spaces for punctuation;

- html-text can add newlines (e.g. after headers or paragraphs), so
that the output text looks more like how it is rendered in browsers.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files html_text

%check 
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
 
%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 18 2024 Benson Muite <benson_muite@emailplus.org> - 0.6.2-1
- Initial packaging
