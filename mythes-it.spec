Name:         mythes-it
Summary:      Italian thesaurus
Version:      5.1.1
Release:      %autorelease
# The license text is embedded within the README files
# Here we specify the thesaurus license only as other files are not packaged 
License:      GPL-3.0-only
URL:          https://pagure.io/dizionario_italiano
Source:       %{url}/archive/%{version}/dizionario_italiano-%{version}.tar.gz

BuildArch:    noarch
Requires:     mythes
Supplements:  (mythes and langpacks-it)

%description
Italian thesaurus.


%prep
%autosetup -n dizionario_italiano-%{version}


%build
# Nothing to do


%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_it_IT_v2.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_it_IT_v2.dat
cp -p th_it_IT_v2.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_it_IT_v2.idx

pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
it_IT_aliases="it_CH"
for lang in $it_IT_aliases; do
        ln -s th_it_IT_v2.dat "th_"$lang"_v2.dat"
        ln -s th_it_IT_v2.idx "th_"$lang"_v2.idx"
done


%files
%license LICENSES/gpl-3.0.txt
%doc CHANGELOG.txt README.md README_th_it_IT.txt
%{_datadir}/mythes/th_it_IT_v2.*
%{_datadir}/mythes/th_it_CH_v2.*

%changelog
%autochangelog
