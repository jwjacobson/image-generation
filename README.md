# Image generation script

This script lets you generate images using Hugging Face's Inference API via the command line. By default, it uses Stable Diffusion to generate images.

## Prerequisites
1. [git](https://git-scm.com/downloads) (to clone the repo)
2. [uv](https://docs.astral.sh/uv/getting-started/installation/) (to manage dependencies and Python versions)
3. A [Hugging Face account](https://huggingface.co/) and valid [API key](https://huggingface.co/settings/tokens)
> [!NOTE]
> The Hugging Face inference API is free to use within certain limits but incurs a charge per request over those limits. You can check your usage in your [account settings](https://huggingface.co/settings/billing).

## Installation
[Clone this repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) and navigate to the image-generation directory:
```bash
git clone git@github.com:jwjacobson/image-generation.git && cd image-generation
```

Create a `.env` file from the provided template:
```bash
cp env-template .env
```

In the `.env` file, paste your API token after `API_TOKEN=`

> [!WARNING]
> Your API key is sensitive data and should not be put in version control. `.env` is already listed in `.gitignore`, but you should be mindful and not expose it.

## Running the script
Type,
```bash
uv run main.py
```
then type your image prompt! The image will be saved as `generated_image.png`

## Adjusting parameters
This script includes two adjustable parameters that affect how the model interprets your prompt: `guidance_scale` and `num_inference_steps`.

*guidance_scale* controls how literally the model interprets your prompt: a lower number is more creative, while a higher one is more literal. 7.5–15 are recommended values.

*num_inference_steps* controls how many times the model refines its output: lower runs quickly but is rougher in quality, while higher is the opposite. 20–30 are good values if you're just playing around. If you know what you want and are willing to wait, try going up to 100!

For simplicity, these values are **hard-coded** into the script, i.e. explicitly declared as part of the code. Simply edit the values in lines 17–18 to experiment.

### License
This script is [free software](https://www.fsf.org/about/what-is-free-software), released under version 3.0 of the GPL. Everyone has the right to use, modify, and distribute gfetch subject to the [stipulations](https://github.com/jwjacobson/image-generation/blob/main/LICENSE) of that license.