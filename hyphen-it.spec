Name:           hyphen-it
Summary:        Italian hyphenation rules
Version:        5.1.1
Release:        %autorelease
# The license text is embedded within the README files
# Here we specify the thesaurus license only as other files are not packaged 
License:        LGPL-2.1-only
URL:            https://pagure.io/dizionario_italiano
Source:         %{url}/archive/%{version}/dizionario_italiano-%{version}.tar.gz

BuildArch:      noarch
Requires:       hyphen
Supplements:    (hyphen and langpacks-it)
Provides:       hyphen-la = %{version}

%description
Italian hyphenation rules.


%prep
%autosetup -n dizionario_italiano-%{version}


%build
# Nothing to do


%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_it_IT.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen
pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
#http://extensions.services.openoffice.org/project/dict-la uses the it_IT for Latin
#so we'll do the same
it_IT_aliases="it_CH la_VA"
for lang in $it_IT_aliases; do
        ln -s hyph_it_IT.dic "hyph_"$lang".dic"
done


%files
%license LICENSES/lgpl-2.1.txt
%doc CHANGELOG.txt README.md README_hyph_it_IT.txt
%{_datadir}/hyphen/hyph_it_IT.dic
%{_datadir}/hyphen/hyph_it_CH.dic
%{_datadir}/hyphen/hyph_la_VA.dic


%changelog
%autochangelog
