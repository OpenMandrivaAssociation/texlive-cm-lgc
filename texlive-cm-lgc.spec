%global tl_name cm-lgc
%global tl_revision 28250

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	Type 1 CM-based fonts for Latin, Greek and Cyrillic
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/ps-type1/cm-lgc
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cm-lgc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cm-lgc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The fonts are converted from Metafont sources of the Computer Modern
font families, using textrace. Supported encodings are: T1 (Latin), T2A
(Cyrillic), LGR (Greek) and TS1. The package also includes Unicode
virtual fonts for use with Omega. The font set is not a replacement for
any of the other Computer Modern-based font sets (for example, cm-super
for Latin and Cyrillic, or cbgreek for Greek), since it is available at
a single size only; it offers a compact set for 'general' working. The
fonts themselves are encoded to external standards, and virtual fonts
are provided for use with TeX.

