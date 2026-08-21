%global fontname google-noto-emoji

BuildRequires:  gcc
BuildRequires:  fontpackages-devel

# Version as found in the font file:
# $ otfinfo -v static/NotoEmoji-Regular.ttf
# Version 3.005
Version: 3.005
Release: %autorelease
Epoch:   1
URL:     https://github.com/googlefonts/noto-emoji

%global foundry           Google
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          README.txt

%global fontfamily0       Noto Emoji
%global fontsummary0      Google “Noto Emoji” Black-and-White emoji font
%global fonts0            NotoEmoji-Regular.ttf
%global fontdescription0  %{expand:
This package provides the Google “Noto Emoji” Black-and-White emoji font.
}

%global fontfamily1       Noto Emoji VF
%global fontsummary1      Google “Noto Emoji” Black-and-White emoji variable font
%global fonts1            NotoEmoji-VariableFont_wght.ttf
%global fontdescription1  %{expand:
This package provides the Google “Noto Emoji” Black-and-White emoji variable font.
}

# Download Noto_Emoji.zip from https://fonts.google.com/selection?query=Noto+emoji
# and check the font versions in the .zip file for example with:
# $ otfinfo -v NotoEmoji-VariableFont_wght.ttf
# Version 3.005
# $ otfinfo -v static/NotoEmoji-Regular.ttf
# Version 3.005
# then rename the .zip file:
Source0: Noto_Emoji-%{version}.zip


%fontpkg -a

%prep
%autosetup -T -c -n noto-emoji-%{version}
unzip %{SOURCE0}
cp -p static/NotoEmoji-Regular.ttf .

%build

%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a


%changelog
%autochangelog
