Name:           dot2tex
Version:        2.11.3
Release:        %autorelease
Summary:        A Graphviz to LaTeX converter
License:        MIT
URL:            http://www.fauskes.net/code/dot2tex/
Source0:        https://github.com/kjellmf/dot2tex/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

Requires:       tex(preview.sty)
Requires:       tex(tikz.sty)

%generate_buildrequires
%pyproject_buildrequires


%description
Dot2tex is a tool for converting graphs rendered by Graphviz to formats
that can be used with LaTeX.

%prep
%setup -q


%build
%pyproject_wheel
find docs examples -name "*.tex" -o -name "*.dot" | xargs sed -i -e 's|\r||'

%install
%pyproject_install


%files
%license LICENSE
%doc examples docs
%{_bindir}/dot2tex
%{python3_sitelib}/%{name}/
%{python3_sitelib}/*.dist-info


%changelog
%autochangelog
