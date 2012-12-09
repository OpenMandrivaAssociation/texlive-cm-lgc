# revision 15878
# category Package
# catalog-ctan /fonts/ps-type1/cm-lgc
# catalog-date 2008-06-12 19:44:55 +0200
# catalog-license gpl
# catalog-version 0.5
Name:		texlive-cm-lgc
Version:	0.5
Release:	2
Summary:	Type 1 CM-based fonts for Latin, Greek and Cyrillic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ps-type1/cm-lgc
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cm-lgc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cm-lgc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The fonts are converted from MetaFont sources of the Computer
Modern font families, using textrace. Supported encodings are:
T1 (Latin), T2A (Cyrillic), LGR (Greek) and TS1. The package
also includes Unicode virtual fonts for use with Omega. The
font set is not a replacement for any of the other Computer
Modern-based font sets (for example, cm-super for Latin and
Cyrillic, or cbgreek for Greek), since it is available at a
single size only; it offers a compact set for 'general'
working. The fonts themselves are encoded to external
standards, and virtual fonts are provided for use with TeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmb6y.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmb6z.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmb8a.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmbc6y.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmbc6z.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmbc8a.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmbcpg.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmbi6y.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmbi6z.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmbi8a.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmbij6y.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmbij6z.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmbij8a.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmbijpg.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmbipg.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmbpg.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmr6y.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmr6z.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmr8a.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmrc6y.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmrc6z.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmrc8a.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmrcpg.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmri6y.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmri6z.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmri8a.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmrij6y.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmrij6z.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmrij8a.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmrijpg.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmripg.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcmrpg.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcsb6y.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcsb6z.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcsb8a.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcsbo6y.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcsbo6z.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcsbo8a.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcsbopg.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcsbpg.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcsr6y.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcsr6z.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcsr8a.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcsro6y.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcsro6z.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcsro8a.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcsropg.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fcsrpg.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fctr6y.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fctr6z.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fctr8a.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fctrc6y.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fctrc6z.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fctrc8a.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fctrcpg.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fctri6y.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fctri6z.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fctri8a.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fctrij6y.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fctrij6z.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fctrij8a.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fctrijpg.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fctripg.afm
%{_texmfdistdir}/fonts/afm/public/cm-lgc/fctrpg.afm
%{_texmfdistdir}/fonts/enc/dvips/cm-lgc/8r-mod.enc
%{_texmfdistdir}/fonts/map/dvips/cm-lgc/cm-lgc.map
%{_texmfdistdir}/fonts/ofm/public/cm-lgc/fcmbcut.ofm
%{_texmfdistdir}/fonts/ofm/public/cm-lgc/fcmbiut.ofm
%{_texmfdistdir}/fonts/ofm/public/cm-lgc/fcmbut.ofm
%{_texmfdistdir}/fonts/ofm/public/cm-lgc/fcmrcut.ofm
%{_texmfdistdir}/fonts/ofm/public/cm-lgc/fcmriut.ofm
%{_texmfdistdir}/fonts/ofm/public/cm-lgc/fcmrut.ofm
%{_texmfdistdir}/fonts/ofm/public/cm-lgc/fcsbout.ofm
%{_texmfdistdir}/fonts/ofm/public/cm-lgc/fcsbut.ofm
%{_texmfdistdir}/fonts/ofm/public/cm-lgc/fcsrout.ofm
%{_texmfdistdir}/fonts/ofm/public/cm-lgc/fcsrut.ofm
%{_texmfdistdir}/fonts/ofm/public/cm-lgc/fctrcut.ofm
%{_texmfdistdir}/fonts/ofm/public/cm-lgc/fctriut.ofm
%{_texmfdistdir}/fonts/ofm/public/cm-lgc/fctrut.ofm
%{_texmfdistdir}/fonts/ovf/public/cm-lgc/fcmbcut.ovf
%{_texmfdistdir}/fonts/ovf/public/cm-lgc/fcmbiut.ovf
%{_texmfdistdir}/fonts/ovf/public/cm-lgc/fcmbut.ovf
%{_texmfdistdir}/fonts/ovf/public/cm-lgc/fcmrcut.ovf
%{_texmfdistdir}/fonts/ovf/public/cm-lgc/fcmriut.ovf
%{_texmfdistdir}/fonts/ovf/public/cm-lgc/fcmrut.ovf
%{_texmfdistdir}/fonts/ovf/public/cm-lgc/fcsbout.ovf
%{_texmfdistdir}/fonts/ovf/public/cm-lgc/fcsbut.ovf
%{_texmfdistdir}/fonts/ovf/public/cm-lgc/fcsrout.ovf
%{_texmfdistdir}/fonts/ovf/public/cm-lgc/fcsrut.ovf
%{_texmfdistdir}/fonts/ovf/public/cm-lgc/fctrcut.ovf
%{_texmfdistdir}/fonts/ovf/public/cm-lgc/fctriut.ovf
%{_texmfdistdir}/fonts/ovf/public/cm-lgc/fctrut.ovf
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmb6a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmb6y.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmb6z.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmb8c.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmb8r.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbc6a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbc6y.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbc6z.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbc8r-nokern.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbc8r.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbcgr.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbcpg.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbgr.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbi6a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbi6y.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbi6z.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbi8c.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbigr.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbij6z.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbij8a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbij8r-nokern.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbij8r.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbipg.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmbpg.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmr6a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmr6y.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmr6z.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmr8a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmr8c.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmr8r.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmrc6a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmrc6y.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmrc6z.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmrc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmrc8r-nokern.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmrc8r.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmrc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmrcgr.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmrcpg.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmrgr.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmri6a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmri6y.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmri6z.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmri8a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmri8c.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmri8r.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmrigr.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmrij6z.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmrij8a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmrij8r-nokern.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmrij8r.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmripg.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcmrpg.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsb6a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsb6y.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsb6z.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsb8c.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsb8r.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsbgr.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsbo6a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsbo6y.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsbo6z.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsbo8a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsbo8c.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsbo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsbo8t.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsbogr.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsbopg.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsbpg.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsr6a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsr6y.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsr6z.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsr8a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsr8c.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsr8r.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsrgr.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsro6a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsro6y.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsro6z.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsro8a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsro8c.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsro8r.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsro8t.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsrogr.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsropg.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fcsrpg.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctr6a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctr6y.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctr6z.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctr8a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctr8c.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctr8r.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctrc6a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctrc6y.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctrc6z.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctrc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctrc8r-nokern.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctrc8r.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctrc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctrcgr.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctrcpg.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctrgr.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctri6a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctri6y.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctri6z.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctri8a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctri8c.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctri8r.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctrigr.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctrij6z.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctrij8a.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctrij8r-nokern.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctrij8r.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctripg.tfm
%{_texmfdistdir}/fonts/tfm/public/cm-lgc/fctrpg.tfm
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmb6y.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmb6y.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmb6z.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmb6z.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmb8a.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmb8a.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbc6y.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbc6y.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbc6z.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbc6z.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbc8a.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbc8a.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbcpg.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbcpg.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbi6y.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbi6y.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbi6z.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbi6z.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbi8a.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbi8a.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbij6y.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbij6y.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbij6z.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbij6z.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbij8a.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbij8a.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbijpg.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbijpg.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbipg.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbipg.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbpg.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmbpg.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmr6y.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmr6y.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmr6z.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmr6z.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmr8a.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmr8a.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmrc6y.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmrc6y.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmrc6z.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmrc6z.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmrc8a.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmrc8a.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmrcpg.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmrcpg.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmri6y.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmri6y.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmri6z.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmri6z.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmri8a.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmri8a.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmrij6y.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmrij6y.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmrij6z.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmrij6z.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmrij8a.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmrij8a.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmrijpg.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmrijpg.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmripg.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmripg.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmrpg.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcmrpg.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsb6y.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsb6y.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsb6z.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsb6z.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsb8a.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsb8a.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsbo6y.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsbo6y.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsbo6z.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsbo6z.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsbo8a.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsbo8a.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsbopg.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsbopg.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsbpg.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsbpg.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsr6y.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsr6y.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsr6z.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsr6z.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsr8a.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsr8a.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsro6y.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsro6y.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsro6z.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsro6z.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsro8a.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsro8a.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsropg.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsropg.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsrpg.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fcsrpg.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctr6y.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctr6y.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctr6z.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctr6z.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctr8a.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctr8a.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctrc6y.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctrc6y.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctrc6z.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctrc6z.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctrc8a.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctrc8a.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctrcpg.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctrcpg.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctri6y.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctri6y.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctri6z.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctri6z.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctri8a.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctri8a.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctrij6y.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctrij6y.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctrij6z.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctrij6z.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctrij8a.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctrij8a.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctrijpg.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctrijpg.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctripg.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctripg.pfb
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctrpg.inf
%{_texmfdistdir}/fonts/type1/public/cm-lgc/fctrpg.pfb
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcmb6a.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcmb8c.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcmb8t.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcmbc6a.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcmbc8t.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcmbcgr.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcmbgr.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcmbi6a.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcmbi8c.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcmbi8t.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcmbigr.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcmr6a.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcmr8c.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcmr8t.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcmrc6a.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcmrc8t.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcmrcgr.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcmrgr.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcmri6a.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcmri8c.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcmri8t.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcmrigr.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcsb6a.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcsb8c.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcsb8t.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcsbgr.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcsbo6a.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcsbo8c.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcsbo8t.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcsbogr.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcsr6a.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcsr8c.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcsr8t.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcsrgr.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcsro6a.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcsro8c.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcsro8t.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fcsrogr.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fctr6a.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fctr8c.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fctr8t.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fctrc6a.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fctrc8t.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fctrcgr.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fctrgr.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fctri6a.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fctri8c.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fctri8t.vf
%{_texmfdistdir}/fonts/vf/public/cm-lgc/fctrigr.vf
%{_texmfdistdir}/tex/latex/cm-lgc/antcmlgc.sty
%{_texmfdistdir}/tex/latex/cm-lgc/cmlgc.sty
%{_texmfdistdir}/tex/latex/cm-lgc/lgrfcm.fd
%{_texmfdistdir}/tex/latex/cm-lgc/lgrfcs.fd
%{_texmfdistdir}/tex/latex/cm-lgc/lgrfct.fd
%{_texmfdistdir}/tex/latex/cm-lgc/t1fcm.fd
%{_texmfdistdir}/tex/latex/cm-lgc/t1fcs.fd
%{_texmfdistdir}/tex/latex/cm-lgc/t1fct.fd
%{_texmfdistdir}/tex/latex/cm-lgc/t2afcm.fd
%{_texmfdistdir}/tex/latex/cm-lgc/t2afcs.fd
%{_texmfdistdir}/tex/latex/cm-lgc/t2afct.fd
%{_texmfdistdir}/tex/latex/cm-lgc/ts1fcm.fd
%{_texmfdistdir}/tex/latex/cm-lgc/ts1fcs.fd
%{_texmfdistdir}/tex/latex/cm-lgc/ts1fct.fd
%{_texmfdistdir}/tex/latex/cm-lgc/ut1fcm.fd
%{_texmfdistdir}/tex/latex/cm-lgc/ut1fcs.fd
%{_texmfdistdir}/tex/latex/cm-lgc/ut1fct.fd
%doc %{_texmfdistdir}/doc/latex/cm-lgc/COPYING
%doc %{_texmfdistdir}/doc/latex/cm-lgc/HISTORY
%doc %{_texmfdistdir}/doc/latex/cm-lgc/INSTALL
%doc %{_texmfdistdir}/doc/latex/cm-lgc/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.5-2
+ Revision: 750311
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.5-1
+ Revision: 718081
- texlive-cm-lgc
- texlive-cm-lgc
- texlive-cm-lgc
- texlive-cm-lgc
- texlive-cm-lgc

