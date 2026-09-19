%global unicodedir %{_datadir}/unicode
%global emojidir %{unicodedir}/emoji

Name:           unicode-emoji
Version:        18.0.0
Release:        %autorelease
Summary:        Unicode Emoji Data Files

License:        Unicode-DFS-2016
URL:            http://www.unicode.org/emoji/
Source0:        https://www.unicode.org/license.txt
Source1:        https://www.unicode.org/Public/%{version}/ucd/emoji/ReadMe.txt
Source2:        https://www.unicode.org/Public/%{version}/ucd/emoji/emoji-data.txt
Source3:        https://www.unicode.org/Public/%{version}/emoji/emoji-sequences.txt
Source4:        https://www.unicode.org/Public/%{version}/emoji/emoji-test.txt
Source5:        https://www.unicode.org/Public/%{version}/ucd/emoji/emoji-variation-sequences.txt
Source6:        https://www.unicode.org/Public/%{version}/emoji/emoji-zwj-sequences.txt
BuildArch:      noarch

%description
Unicode Emoji Data Files are the machine-readable
emoji data files associated with
http://www.unicode.org/reports/tr51/index.html

%prep
%{nil}

%build
%{nil}

%install
cp -p %{SOURCE0} .
mkdir -p %{buildroot}%{emojidir}
cp -p %{SOURCE1} %{buildroot}%{emojidir}
cp -p %{SOURCE2} %{buildroot}%{emojidir}
cp -p %{SOURCE3} %{buildroot}%{emojidir}
cp -p %{SOURCE4} %{buildroot}%{emojidir}
cp -p %{SOURCE5} %{buildroot}%{emojidir}
cp -p %{SOURCE6} %{buildroot}%{emojidir}

%files
%license license.txt
%dir %{unicodedir}
%dir %{emojidir}
%doc %{emojidir}/ReadMe.txt
%{emojidir}/emoji-*txt

%changelog
%autochangelog
