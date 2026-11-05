Version:        1.9.1
Release:        %autorelease
URL:            https://vercel.com/font

%global foundry vercel
%global fontlicense OFL-1.1
%global fontlicenses geist-font/OFL.txt
%global fontdocsex %{fontlicenses}

%global sans_description %{expand:Geist is a sans-serif typeface designed for
legibility and simplicity. It is a modern, geometric typeface that is based on
the principles of classic Swiss typography. It is designed to be used in
headlines, logos, posters, and other large display sizes.}

%global mono_description %{expand:Geist Mono is a monospaced typeface that has
been crafted to be the perfect partner to Geist Sans. It is designed to be used
in code editors, diagrams, terminals, and other text-based interfaces where code
is represented.}

%global fontfamily0 Geist
%global fontsummary0 The Geist font family
%global fonts0 geist-font/Geist/otf/*.otf
%global fontconfs0 %{SOURCE10}
%global fontdescription0 %{expand:%{sans_description}

This package contains the Geist font family.}

%global fontfamily1 Geist VF
%global fontsummary1 The Geist font family (variable)
%global fonts1 geist-font/Geist/variable/*.ttf
%global fontconfs1 %{SOURCE11}
%global fontdescription1 %{expand:%{sans_description}

This package contains the variable Geist font family.}

%global fontfamily2 Geist Mono
%global fontsummary2 The Geist Mono font family
%global fonts2 geist-font/GeistMono/otf/*.otf
%global fontconfs2 %{SOURCE12}
%global fontdescription2 %{expand:%{mono_description}

This package contains the Geist Mono font family.}

%global fontfamily3 Geist Mono VF
%global fontsummary3 The Geist Mono font family (variable)
%global fonts3 geist-font/GeistMono/variable/*.ttf
%global fontconfs3 %{SOURCE13}
%global fontdescription3 %{expand:%{mono_description}

This package contains the variable Geist Mono font family.}

%global fontfamily4 Geist Pixel
%global fontsummary4 The Geist Pixel font family
%global fonts4 geist-font/GeistPixel/otf/*.otf
%global fontconfs4 %{SOURCE14}
%global fontdescription4 %{expand:Geist Pixel is a pixel typeface available in Circle, Triangle, Line, Grid,
and Square designs.

This package contains the Geist Pixel font family.}

%global fontfamily5 Geist Pixel VF
%global fontsummary5 The Geist Pixel font family (variable)
%global fonts5 geist-font/GeistPixel/variable/*.ttf
%global fontconfs5 %{SOURCE15}
%global fontdescription5 %{expand:Geist Pixel is a pixel typeface available in Circle, Triangle, Line, Grid,
and Square designs.

This package contains the variable Geist Pixel font family.}

%global fontfamily6 Geist Serif
%global fontsummary6 The Geist Serif font family
%global fonts6 geist-font/GeistSerif/ttf/*.ttf
%global fontconfs6 %{SOURCE16}
%global fontdescription6 %{expand:Geist Serif is a serif typeface available in Regular, Triangle, Square,
and Heart designs.

This package contains the Geist Serif font family.}

%global fontfamily7 Geist Serif VF
%global fontsummary7 The Geist Serif font family (variable)
%global fonts7 geist-font/GeistSerif/variable/*.ttf
%global fontconfs7 %{SOURCE17}
%global fontdescription7 %{expand:Geist Serif is a serif typeface available in Regular, Triangle, Square,
and Heart designs.

This package contains the variable Geist Serif font family.}

Source0:        https://github.com/vercel/geist-font/releases/download/v%{version}/geist-font-v%{version}.zip
Source10:       63-vercel-geist.conf
Source11:       63-vercel-geist-vf.conf
Source12:       63-vercel-geist-mono.conf
Source13:       63-vercel-geist-mono-vf.conf
Source14:       63-vercel-geist-pixel.conf
Source15:       63-vercel-geist-pixel-vf.conf
Source16:       63-vercel-geist-serif.conf
Source17:       63-vercel-geist-serif-vf.conf

%fontpkg -a

%prep
%autosetup -c

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a
%fontfiles -a

%changelog
%autochangelog
